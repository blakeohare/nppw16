ACORN_SPEED = 1.5

class AcornAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.countdown = int(random.random() * 5 * 30)
		self.mode = 'patrolling' # patrolling | throwing | baldpatrolling
		self.top = None
		self.walkingLeft = True
	
	def doStuff(self, scene):
		self.countdown -= 1
		walk = False
		if self.mode == 'patrolling':
			if self.countdown <= 0:
				self.mode = 'throwing'
				self.top = Sprite('acorntop', self.sprite.x, self.sprite.y)
				self.top.acorntopdir = self.sprite.lastDirection
				self.top.goLeft = self.top.acorntopdir == 'left'
				self.top.automation.body = self.sprite
				self.top.deleteWhenOffScreen = True
				self.top.ghost = True
				self.top.floats = True
				self.sprite.spawns = [self.top]
			else:
				walk = True
		elif self.mode == 'throwing':
			if self.top.dead:
				self.mode = 'baldpatrolling'
		elif self.mode == 'baldpatrolling':
			walk = True
		
		if walk:
			if self.sprite.collidedWall:
				self.walkingLeft = not self.walkingLeft
			
			tiles = scene.tiles
			cols = scene.cols
			rows = scene.rows
			dx = ACORN_SPEED if self.walkingLeft else -ACORN_SPEED
			oldTileX = int(self.sprite.modelX / 16)
			newX = self.sprite.modelX + dx
			oldTileY = int(self.sprite.modelY / 16)
			newTileX = int(newX / 16)
			if newTileX < 0 or newTileX >= cols:
				self.walkingLeft = not self.walkingLeft
				return
			
			belowTileY = oldTileY + 1
			
			if newTileX == oldTileX:
				self.sprite.dx = dx
			else:
				if belowTileY < 0 or belowTileY >= rows:
					pass
				if not tiles[newTileX][belowTileY].solid:
					self.walkingLeft = not self.walkingLeft
					pass
				else:
					self.sprite.dx = dx
			
			# TODO: walk back and forth, but don't fall off.
