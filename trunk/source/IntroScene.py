# TODO: intro slide show

class IntroScene:
	def __init__(self):
		self.flags = ''
		self.next = self
	
	def processInput(self, events, pressedKeys):
		pass 
	
	def update(self):
		self.next = PlayScene('main', 1, 1, Context())
	
	def render(self, screen, rc):
		pass