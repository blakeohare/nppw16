class BirdAutomation:
	def __init__(self, sprite, onBikeLevel):
		sprite.isEnemy = True
		self.counter = 0
		self.mode = 'stalk' # 'right' | 'left'
		self.sprite = sprite
		self.bikeLevel = onBikeLevel
		
	def doStuff(self, scene):
		self.counter += 1
		p = scene.player
		sprite = self.sprite
		if self.mode == 'stalk':
			dy = p.y - self.sprite.y
			
			if abs(dy) < 6:
				self.mode = 'right'
			elif dy > 0:
				self.sprite.dy += 3
			else:
				self.sprite.dy -= 3
		elif self.mode == 'right':
			if sprite.x < p.x:
				sprite.dx = 6
			else:
				self.mode = 'left'
		else: # mode == 'left'
			spriteX = sprite.x
			if self.bikeLevel:
				spriteX -= self.counter * BIKE_SPEED
			
			if spriteX > 7:
				sprite.dx = -6
			else:
				self.mode = 'stalk'
		
		if self.bikeLevel:
			sprite.dx += BIKE_SPEED