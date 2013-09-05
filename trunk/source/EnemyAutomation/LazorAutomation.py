
class LazorAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		
	def doStuff(self, scene):
		vx = self.sprite.bvx
		self.sprite.dx = self.sprite.bvx