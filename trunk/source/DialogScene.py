
class DialogScene:
	def __init__(self, bg, dialogId, slightDelay):
		self.next = self
		self.flags = ''
		self.bg = bg
		self.delayCounter = 45 if slightDelay else 0
		self.stanzas = DIALOGS[dialogId]
		self.stanzaIndex = 0
		self.textCursor = 0
	
	def processInput(self, events, pressed):
		pass
	
	def update(self):
		self.delayCounter -= 1
	
	def render(self, screen, rc):
		self.bg.render(screen, rc)
		
		if self.delayCounter > 0: return
		
		drawBox(screen, 16, 16, 28, 10)