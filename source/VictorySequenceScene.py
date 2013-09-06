class VictorySequenceScene:
	def __init__(self, bg):
		self.next = self
		self.bg = bg
		self.flags = 'M'
	
		self.counter = 0
	
	def processInput(self, events, pressed):
		pass
	
	def update(self):
		pass
	
	def render(self, screen, rc):
		screen.fill((255, 0, 0))