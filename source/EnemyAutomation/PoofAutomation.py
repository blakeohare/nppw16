
class PoofAutomation:
	def __init__(self, sprite, isBig):
		self.sprite = sprite
		self.counter = 0
		self.isBig = isBig
		
	
	def doStuff(self, scene):
		self.counter += 1
		if self.counter == 15:
			self.sprite.dead = True