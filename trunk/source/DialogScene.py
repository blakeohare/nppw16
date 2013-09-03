
class DialogScene:
	def __init__(self, bg, dialogId):
		self.next = self
		self.flags = ''
		self.bg = bg
	
	def processInput(self, events, pressed):
		pass
	
	def update(self):
		pass
	
	def render(self, screen, rc):
		self.bg.render(screen, rc)