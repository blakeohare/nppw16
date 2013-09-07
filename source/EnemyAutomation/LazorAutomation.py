
class LazorAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		
	def doStuff(self, scene):
		vx = self.sprite.bvx
		self.sprite.dx = self.sprite.bvx
		if scene.id == 'bike_level':
			self.sprite.dx += 5