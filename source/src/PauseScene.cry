class PauseScene:
	def __init__(self, bg):
		self.bg = bg
		self.next = self
		self.flags = ''
		self.counter = 0
	
	def processInput(self, events, pressed):
		for event in events:
			if event.down and event.action == 'start':
				if 'M' in self.bg.flags:
					playNoise('pause_sound')
					pygame.mixer.music.unpause()
				self.next = self.bg
				self.bg.next = self.bg
	
	def update(self):
		if 'M' in self.bg.flags:
			if self.counter == 0:
				pygame.mixer.music.pause()
				playNoise('pause_sound')
		
		self.counter += 1
	
	def render(self, screen, rc):
		screen.fill(BLACK)
		img = getText(WHITE, "PAUSE")
		x = 128 - img.get_width() // 2
		y = 112 - img.get_height() // 2
		screen.blit(img, (x, y))