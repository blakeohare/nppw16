class TitleScene:
	def __init__(self):
		self.next = self
		self.flags = ''
		self.flash_counter = 0
	
	def processInput(self, events, pressedKeys):
		for event in events:
			if self.flash_counter < 0 and event.down and event.action == 'start':
				self.flash_counter = 30
				# TODO: play sound
	
	def update(self):
		self.flash_counter -= 1
		if self.flash_counter == 1:
			self.next = IntroScene()
	
	def render(self, screen, renderCounter):
		screen.fill((0, 0, 0))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(10, 10, 50, 50))
		
		img = renderText((255, 255, 255), "Hello, World!")
		screen.blit(img, (100, 100))
		
		screen.fill((0, 0, 0))
		screen.blit(getImage('slides/title.png'), (0, 0))
		
		showText = (renderCounter // 10) % 3 != 0
		if self.flash_counter > 0:
			showText = renderCounter % 4 < 2
		if showText:
			pressStart = renderText((255, 255, 255), "< Press Start >")
			
			x = (screen.get_width() - pressStart.get_width()) // 2
			screen.blit(pressStart, (x, 140))