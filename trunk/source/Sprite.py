NEIGHBOR_RANGE = (-1, 0, 1)

SPRITE_HEIGHT = {
	'player_side': 32
}

G = 0.7

def getSpriteHeight(type):
	return SPRITE_HEIGHT.get(type, 16)


def SPRITE_renderPlayerOver(sprite, scene, screen, offsetX, offsetY, rc):
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	width = 16
	height = 16
	if scene.side:
		top -= 16
		height = 32
	
	pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(left, top, width, height))

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

class Sprite:
	def __init__(self, type, px, py):
		self.type = type
		self.x = px
		self.y = py
		self.modelX = px + 0.0
		self.modelY = py + 0.0
		self.xs = [None] * 5
		self.ys = [None] * 5
		self.vy = 0
		self.onGround = False
		self.neighbors = [None] * 36
		self.renderImpl = SPRITE_renderPlayerOver
		self.dx = 0
		self.dy = 0
		
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
		if scene.side:
			# hotspot is located in the center of the bottom most tile
			areaX = self.modelX
			areaBottom = self.modelY + 8
			heightFromHotSpot = getSpriteHeight(self.type) - 8 - 4
			areaTop = self.modelY - heightFromHotSpot
			
			width = scene.cols
			height = scene.rows
			
			# side-to-side calcuation is done first, independent of whether you are on the ground.
			if self.dx != 0:
				newX = self.modelX + self.dx
				# isCollision ignores collisions near the sprite's feet
				# if you are near ground, you will be automatically placed standing
				# upon it at the end of the vertical adjustment phase.
				if not scene.isCollision(newX, areaTop, newX, areaBottom):
					self.modelX = newX
			
			# vertical adjustment phase
			# assume sprite is flying through the air unless you see ground
			wasOnGround = self.onGround # save the previous ground state. If you weren't on ground before but suddenly are, then you "landed" and a sound should be played. 
			self.onGround = False
			if wasOnGround:
				self.vy = 0
			else:
				self.vy += G
			
			self.dy += self.vy
			
			if self.dy > 10:
				self.dy = 10
			
			tileX = int(self.modelX / 16)
			
			newBottom = areaBottom + self.dy
			newTop = areaTop + self.dy
			no = False
			if self.dy < 0:
				# Going Up
				if newTop < 0:
					# TODO: do top transitions here.
					no = True
				else:
					newTileTop = int(newTop / 16)
					if scene.tiles[tileX][newTileTop].solid:	
						no = False
						self.vy = 0
						playNoise('hit_head')
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
					playNoise('DEATH')
					scene.next = DeathScene()
					no = True
				else:
					if scene.tiles[tileX][newTileBottom].solid:
						no = True
						self.onGround = True
						self.modelY = newTileBottom * 16 - 8
						if not wasOnGround:
							playNoise('land_on_ground')
					
			if not no:
				self.modelY = newBottom - 8
			self.x = int(self.modelX)
			self.y = int(self.modelY)
		else:
			if self.dx != 0 or self.dy != 0:
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
		self.renderImpl(self, scene, screen, offsetX, offsetY, rc)