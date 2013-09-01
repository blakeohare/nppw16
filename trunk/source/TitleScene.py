class TitleScene:
	def __init__(self):
		self.next = self
	
	def processInput(self, events, pressedKeys):
		pass
	
	def update(self):
		pass
	
	def render(self, screen, renderCounter):
		screen.fill((0, 0, 0))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(10, 10, 50, 50))