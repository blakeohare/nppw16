class ByatAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.perched = False
		self.counter = 0
		self.mode = 'perch'
		self.perched = True
		self.dropHeight = 10
		
	def doStuff(self, scene):
		self.counter += 1
		sprite = self.sprite
		tiles = scene.tiles
		
		if self.mode == 'perch':
			self.perched = True
			if self.counter > 3 * 30:
				self.counter = 0
				self.mode = 'down'
				self.perched = False
				dropHeight = int(random.random() * 5 + 1) * 16
				self.targetY = sprite.y + dropHeight
				#self.originalY = sprite.y
				
		elif self.mode == 'down':
			sprite.dy = 2
			if sprite.y >= self.targetY or sprite.collidedWall or sprite.onGround:
				self.mode = 'swoop'
				self.counter = 0
				self.swoopLeft = scene.player.x < sprite.x
		elif self.mode == 'swoop':
			swoopSpeed = 1.6
			sprite.dy = math.sin(self.counter * 40 / (2 * 3.14159)) * 4
			sprite.dx = -swoopSpeed if self.swoopLeft else swoopSpeed
			if self.counter > 30 * 6:
				self.mode = 'up'
				self.counter = 0
			elif sprite.collidedWall:
				self.swoopLeft = not self.swoopLeft
		
		elif self.mode == 'up':
			sprite.dy = -3.5
			mt = sprite.x & 15
			if mt < 4:
				sprite.dx = 1
			elif mt > 12:
				sprite.dx = -1
			stop = False
			if self.sprite.collidedWall:
				stop = True
			else:
				tx = sprite.x // 16
				ty = (sprite.y - 8) // 16
				if tx < 0 or tx >= scene.cols or ty < 0 or ty >= scene.rows:
					stop = True
				else:
					t = tiles[tx][ty]
					if t.isTop or t.solid:
						stop = True
			
			if stop:
				self.mode = 'perch'
				self.counter = 0
		