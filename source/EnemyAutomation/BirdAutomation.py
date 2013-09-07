class Bird1Automation:
	def __init__(self, sprite):
		sprite.isEnemy = True
		self.counter = 0
		self.mode = 'stalk' # 'right' | 'left'
		self.sprite = sprite
		
	def doStuff(self, scene):
		p = scene.player
		sprite = self.sprite
		if self.mode == 'stalk':
			dy = p.y - self.sprite.y
			if abs(dy < 6):
				self.counter = 0
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
			if sprite.x > 7:
				sprite.dx = -6
			else:
				self.mode = 'stalk'