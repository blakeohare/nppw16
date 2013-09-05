NEIGHBOR_RANGE = (-1, 0, 1)

JUMPING_VY = -14
RUN_JUMPING_VY = -16
WATER_JUMPING_VY = -5

SPRITE_HEIGHT = {
	'player_side': 32,
	'acorn': 16,
	'acorntop': 16,
	'gravity_device': 16,
	'lazor': 16
}

G = 0.7
STRONG_G = 1.55
WATER_G = 0.3

def getSpriteHeight(type):
	return SPRITE_HEIGHT.get(type, 16)

XY_PAIRINGS = [
	(0, 0),
	(1, 0),
	(2, 0),
	(3, 0),
	(4, 0),
	(4, 1),
	(4, 2),
	(4, 3)
]

ENEMY_TYPES = [
	'acorn',
	'acorntop'
]

class Sprite:
	def __init__(self, type, px, py):
		self.type = type
		self.isEnemy = False
		self.height = getSpriteHeight(type)
		self.x = px
		self.y = py
		self.modelX = px + 0.0
		self.modelY = py + 0.0
		self.xs = [None] * 5
		self.ys = [None] * 5
		self.vy = 0
		self.moving = False
		self.lastDirection = 'left'
		self.onGround = False
		self.neighbors = [None] * 36
		self.spawns = None
		self.dead = False
		self.deleteWhenOffScreen = False
		self.ghost = False
		self.renderImpl = SPRITE_renderPlayerOver
		self.automation = None
		self.floats = False
		self.deathState = None
		self.sprinkle = False
		self.isEnemy = type in ENEMY_TYPES
		self.isBullet = type == 'lazor'
		if type == 'acorn':
			self.renderImpl = SPRITE_renderAcorn
			self.automation = AcornAutomation(self)
		elif type == 'acorntop':
			self.renderImpl = SPRITE_renderAcornTop
			self.automation = AcornTopAutomation(self)
			self.acorntopdir = 'left'
		elif type == 'gravity_device':
			self.renderImpl = SPRITE_renderGravityDevice
			self.automation = None
		elif type == 'lazor':
			self.renderImpl = SPRITE_renderLazor
			self.automation = LazorAutomation(self)
			
		self.dx = 0
		self.dy = 0
		self.ddx = 0 # "damage dx", will stay set until you land on the ground or blink counter goes < 0
		self.damageDir = None
		self.cling = False
		self.ladderDY = 0
		self.blinkCounter = -1
		
		
	def checkNeighborCollision(self, scene, col, row, targetX, targetY):
		area_left = targetX - 5
		area_right = targetX + 5
		area_top = targetY - 5
		area_bottom = targetY + 5
		
		width = scene.cols
		height = scene.rows
		left = col - 2
		right = col + 2
		top = row - 2
		bottom = row + 2
		if left < 0: left = 0
		if right >= width: right = width - 1
		if top < 0: top = 0
		if bottom >= height: bottom = height - 1
		index = 0
		y = top
		while y <= bottom:
			x = left
			while x <= right:
				cs = scene.tiles[x][y].collisions
				csi = len(cs) - 1
				while csi >= 0:
					self.neighbors[index] = cs[csi]
					csi -= 1
					index += 1
				x += 1
			y += 1
		
		index -= 1
		while index >= 0:
			n = self.neighbors[index]
			if n[0] > area_right:
				pass
			elif n[1] > area_bottom:
				pass
			elif n[2] < area_left:
				pass
			elif n[3] < area_top:
				pass
			else:
				return False
			index -= 1
		return True
		
	def update(self, scene):
		
		if self.automation != None:
			self.automation.doStuff(scene)
		
		self.blinkCounter -= 1
		if self.blinkCounter < 0 or self.onGround:
			self.ddx = 0
			if self.damageDir != None:
				self.lastDirection = self.damageDir
			self.damageDir = None
		
		if self.damageDir != None:
			self.dx = 0
		
		self.dx += self.ddx
		if scene.side:
			# hotspot is located in the center of the bottom most tile
			areaX = self.modelX
			areaBottom = self.modelY + 8
			heightFromHotSpot = getSpriteHeight(self.type) - 8 - 4
			areaTop = self.modelY - heightFromHotSpot
			
			width = scene.cols
			height = scene.rows
			
			self.moving = self.dx != 0 or self.dy != 0
			
			# side-to-side calcuation is done first, independent of whether you are on the ground.
			if self.dx != 0:
				newX = self.modelX + self.dx
				
				# isCollision ignores collisions near the sprite's feet
				# if you are near ground, you will be automatically placed standing
				# upon it at the end of the vertical adjustment phase.
				if self.ghost or not scene.isCollision(newX, areaTop, newX, areaBottom):
					self.modelX = newX
					if self.dx > 0:
						self.lastDirection = 'right'
					else:
						self.lastDirection = 'left'
				self.dx = 0
			
			tileX = int(self.modelX / 16)
			tileY = int(self.modelY / 16)
			
			offScreen = tileX < 0 or tileX >= scene.cols or tileY < 0 or tileY >= scene.rows
			onScreen = not offScreen
			
			# vertical adjustment phase
			# assume sprite is flying through the air unless you see ground
			wasOnGround = self.onGround # save the previous ground state. If you weren't on ground before but suddenly are, then you "landed" and a sound should be played. 
			self.onGround = False
			if wasOnGround or self.floats:
				self.vy = 0
			else:
				if onScreen and scene.tiles[tileX][tileY].isWater:
					self.vy += WATER_G
				elif scene.context.gravity:
					self.vy += STRONG_G
				else:
					self.vy += G
			
			# If you're clinging to a ladder, then throw out the vy entirely.
			# Use self.ladderDY instead
			if self.cling:
				self.dy = self.ladderDY
				self.vy = 0
			else:
				self.dy += self.vy
			
			oldLadderDY = self.ladderDY
			self.ladderDY = 0
			
			if self.dy > 10:
				self.dy = 10
			elif self.dy < -10:
				self.dy = -10
			
			wasCling = self.cling
			movedUp = False
			
			newBottom = areaBottom + self.dy
			newTop = areaTop + self.dy
			
			no = False
			
			if self.ghost:
				pass # just go with it
			else:
				if self.dy < 0:
					# Going Up
					if newTop < 0:
						# TODO: do top transitions here.
						no = True
					else:
						newTileTop = int(newTop / 16)
						
						offScreen = tileX < 0 or tileX >= scene.cols or newTileTop < 0 or newTileTop >= scene.rows
						onScreen = not offScreen
						
						if onScreen and scene.tiles[tileX][newTileTop].solid:
							no = False
							self.vy = 0
							self.dy = 0
							playNoise('head_bonk')
						else:
							movedUp = True
				else:
					# Going Down (or staying the same)
					# The philosophy here is different. When you encounter a collision,
					# rather than stop the movement, you find where the top of the collided
					# tile is and place the sprite there.
					
					newTileBottom = int(newBottom / 16)
					
					# If the player fell off the bottom
					if newTileBottom >= height:
						# TODO: check if there is a transition registered with the map.
						# If so begin that transition instead of killing the player.
						playNoise('fall_to_death')
						scene.next = DeathOverrideScene(scene, 'fall')
						no = True
					else:
					
						offScreen = tileX < 0 or tileX >= scene.cols or newTileBottom < 0 or newTileBottom >= scene.rows
						onScreen = not offScreen
						
						t = scene.tiles[tileX][newTileBottom]
						topStop = False
						if t.isTop:
							oldTileBottom = int(areaBottom / 16)
							if newTileBottom > oldTileBottom:
								topStop = True
							elif newTileBottom == oldTileBottom and areaBottom == newBottom:
								topStop = True
						if t.solid or topStop:
							no = True
							self.cling = False
							self.onGround = True
							self.modelY = newTileBottom * 16 - 8
							self.vy = 0
							if not wasOnGround:
								playNoise('land_on_ground')
					
			if not no:
				self.modelY = newBottom - 8
			self.x = int(self.modelX)
			self.y = int(self.modelY)
			self.dy = 0
			self.dy = 0
			
			tileY = int(self.modelY / 16)
			
			offScreen = tileX < 0 or tileX >= scene.cols or tileY < 0 or tileY >= scene.rows
			onScreen = not offScreen
			if onScreen and scene.tiles[tileX][tileY].isLadder:
				pass
			else:
				self.cling = False
			
			if movedUp and wasCling and not self.cling:
				self.modelY = 16 * tileY # maybe?
			
		else:
			self.moving = False
			if self.dx != 0 or self.dy != 0:
				self.moving = True
				
				if self.dy < 0:
					self.lastDirection = 'up'
				elif self.dy > 0:
					self.lastDirection = 'down'
				elif self.dx < 0:
					self.lastDirection = 'left'
				else:
					self.lastDirection = 'right'
					
				xs = self.xs
				ys = self.ys
				
				xs[0] = self.modelX + self.dx
				xs[1] = self.modelX + self.dx * 3.0 / 4
				xs[2] = self.modelX + self.dx / 2.0
				xs[3] = self.modelX + self.dx / 4.0
				xs[4] = self.modelX
				
				ys[0] = self.modelY + self.dy
				ys[1] = self.modelY + self.dy * 3.0 / 4
				ys[2] = self.modelY + self.dy / 2.0
				ys[3] = self.modelY + self.dy / 4.0

				for pairing in XY_PAIRINGS:
					newx = xs[pairing[0]]
					newy = ys[pairing[1]]
					col = int(newx / 16)
					row = int(newy / 16)

					if self.checkNeighborCollision(scene, col, row, newx, newy):
						self.modelX = newx
						self.modelY = newy
						self.x = int(self.modelX)
						self.y = int(self.modelY)
						break
				
				self.dx = 0
				self.dy = 0
	
	def render(self, scene, screen, offsetX, offsetY, rc):
		if self.blinkCounter < 0 or (self.blinkCounter & 1) == 0:
			self.renderImpl(self, scene, screen, offsetX, offsetY, rc)
	
	def isCollision(self, other):
		left = self.x - 8
		oleft = other.x - 8
		right = left + 16
		oright = oleft + 16
		
		if left >= oright or right <= oleft:
			return False
		
		bottom = self.y + 8
		obottom = other.y + 8
		top = bottom - self.height
		otop = obottom - other.height
		
		if top >= obottom or otop >= bottom:
			return False
		return True
	
	def hit(self, scene, amount):
		self.blinkCounter = 40
		self.blinkDirection = self.lastDirection
		self.damageDir = self.lastDirection
		if self.lastDirection == 'left':
			self.ddx = 3
		else:
			self.ddx = -3
		self.onGround = False
		self.vy = -6
		scene.context.adjustHealth(scene, -amount)