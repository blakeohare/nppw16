class DeathOverrideScene:
	# type = "lava", "collapse"
	def __init__(self, bg, type):
		self.bg = bg
		self.context = bg.context
		self.flags = ''
		self.next = self
		self.type = type
		self.counter = 0
		self.bg.player.deathState = type
		self.vy = -10
		
		
	def processInput(self, events, pressed):
		pass # There is nothing you can do
	
	def update(self):
		self.counter += 1
		self.vy += 1
		if self.type == 'lava':
			self.bg.player.modelY += self.vy
			self.bg.player.y = int(self.bg.player.modelY)
			
		if self.counter > 100:
			self.context.lifemeter = 10
			self.context.lives -= 1
			if self.context.lives == 0:
				self.context.lives = 3
				self.next = GameOverScene(self.context)
			else:
				self.next = ReadyScene(self.bg, self.context)
			# TODO: game over or beginning of same map at same door entrance
		
	
	def render(self, screen, rc):
		self.bg.render(screen, rc)
	