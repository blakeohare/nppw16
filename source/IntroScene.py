# TODO: intro slide show

class IntroScene:
	def __init__(self):
		self.flags = ''
		self.next = self
	
	def processInput(self, events, pressedKeys):
		pass 
	
	def update(self):
		self.next = PlayScene('ship_1', 8, 8, Context())
	
	def render(self, screen, rc):
		pass