
class AcornTopAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.goLeft = True
		self.countdown = 40
	
	def doStuff(self, scene):
		self.countdown -= 1
		if self.countdown == 0:
			self.goLeft = not self.goLeft
		
		# TODO: "loop" as it approaches 0 and then afterwards, go back to the sender in a straight line
		if self.goLeft:
			self.sprite.dx = -3
		else:
			self.sprite.dx = 3
		
				