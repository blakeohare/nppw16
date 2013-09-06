class GameOverScene:
	def __init__(self, context):
		self.next = self
		self.flags = ''
		self.context = context
		self.counter = 0
		self.index = 0
		self.mode = 'prompt'
		self.password = context.convertToPassword()
		
	def processInput(self, events, pressed):
		if self.mode == 'prompt':
			for event in events:
				if event.down:
					if event.action == 'up':
						if self.index == 1:
							self.index = 0
					elif event.action == 'down':
						if self.index == 0:
							self.index = 1
					elif event.action in ('A', 'B', 'start'):
						self.mode = 'commit'
						self.counter = 0
	
	def update(self):
		JUKEBOX.ensureSong('gameover')
		self.counter += 1
		if self.mode == 'commit':
			if self.counter > 30:
				if self.index == 0:
					self.next = PlayScene('ship_1', 8, 9, self.context)
				elif self.index == 1:
					self.next = TitleScene()
				else:
					# what?
					self.next = OpeningScene()
		
	
	def render(self, screen, rc):
		screen.fill((0, 0, 0))
		show_selected = self.mode == 'prompt' or (rc % 2) == 0
		gameOver = getText(WHITE, "GAME OVER")
		optionA = getText(WHITE, "CONTINUE")
		optionB = getText(WHITE, "END")
		password = getText(WHITE, "PASSWORD:")
		passwordValue = getText((128, 128, 128), self.password)
		cursor = getText(WHITE, ">")
		
		left = 80
		top = 96
		
		x = left
		y = top
		screen.blit(gameOver, (left, top))
		
		y += 16
		if self.index == 0:
			screen.blit(cursor, (x, y))
		if show_selected or self.index == 1:
			screen.blit(optionA, (x + 16, y))
		
		y += 16
		if self.index == 1:
			screen.blit(cursor, (x, y))
		if show_selected or self.index == 0:
			screen.blit(optionB, (x + 16, y))
		
		y += 48
		x -= 32
		screen.blit(password, (x, y))
		x += password.get_width() + 8
		screen.blit(passwordValue, (x, y))