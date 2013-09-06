class WaterPopAutomation:
	def __init__(self, sprite):
		self.counter = 0
		self.sprite = sprite
		
	def doStuff(self, scene):
		self.counter += 1
		if self.counter >= 15:
			self.sprite.dead = True