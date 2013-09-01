class TitleScene:
	def __init__(self):
		self.next = self
		self.flags = ''
	
	def processInput(self, events, pressedKeys):
		pass
	
	def update(self):
		pass
	
	def render(self, screen, renderCounter):
		screen.fill((0, 0, 0))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(10, 10, 50, 50))
		
		img = renderText((255, 255, 255), "Hello, World!")
		screen.blit(img, (100, 100))