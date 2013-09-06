class VictorySequenceScene:
	def __init__(self, bg):
		self.next = self
		self.bg = bg
		self.flags = ''
	
		self.images = [
			getImage('slides/close1.png'),
			getImage('slides/close2.png')]
	
		self.player = None
	
		self.counter = 0
	
	def processInput(self, events, pressed):
		pass
	
	def update(self):
		pygame.mixer.music.stop()
		self.counter += 1
	
	def render(self, screen, rc):
		screen.fill(BLACK)
		if self.counter < 60:
			img = self.images[0]
		elif self.counter > 120:
			img = self.images[1]
		else:
			img = self.images[self.counter & 1]
		
		if self.counter == 60:
			playNoise('screen_shaking')
		
		if self.counter == 150:
			self.next = DialogScene(self, 'CloseDialog', False, True, False)
			self.counter += 1
		
		if self.counter == 160:
			self.next = CreditsScene()
		
		screen.blit(img, (0, 16))
	
	