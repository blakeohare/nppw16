class TitleScene:
	def __init__(self):
		self.next = self
		self.flags = ''
		self.flash_counter = 0
		self.options = [
			('start', 'Start Game'),
			('password', "Enter Password"),
			('joystick', "Configure Game Pad")]
		self.index = 0
			
	def processInput(self, events, pressedKeys):
		for event in events:
			if self.flash_counter < 0:
				if event.down:
					if event.action in ['start', 'A', 'B']:
						self.flash_counter = 30
						playNoise('menu_select')
					elif event.action == 'up':
						if self.index > 0:
							self.index -= 1
							playNoise('menu_move')
					elif event.action == 'down':
						if self.index < 2:
							self.index += 1
							playNoise('menu_move')
					
	
	def update(self):
		self.flash_counter -= 1
		if self.flash_counter == 1:
			action = self.options[self.index][0]
			if action == 'start':
				self.next = IntroScene()
			elif action == 'password':
				self.next = PasswordScene()
			elif action == 'joystick':
				self.next = JoystickMenuScene()
			else:
				pass # Assert! or something.
	
	def render(self, screen, renderCounter):
		
		JUKEBOX.ensureSong('title')
		
		screen.fill((0, 0, 0))
		pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(10, 10, 50, 50))
		
		img = renderText((255, 255, 255), "Hello, World!")
		screen.blit(img, (100, 100))
		
		screen.fill((0, 0, 0))
		screen.blit(getImage('slides/title.png'), (0, 0))
		
		showText = True #(renderCounter // 10) % 3 != 0
		if self.flash_counter > 0:
			showText = renderCounter % 4 < 2
		
		index = 0
		y = 136
		left = 64
		
		drawBox(screen, left - 32, y - 16, 24, 9)
		
		for option in self.options:
			
			if index == self.index:
				screen.blit(getText((255, 255, 255), ">"), (left - 16, y))
			
			if index != self.index or showText:
				screen.blit(getText((255, 255, 255), option[1]), (left, y))
			
			index += 1
			y += 16
		
		y += 32
		active_js = getText((128, 128, 128), "Active joystick: ")
		screen.blit(active_js, (8, y))
		x = 8 + active_js.get_width()
		if active_joystick == None:
			js_name = getText((255, 0, 0), "None")
		else:
			js_name = getText((255, 255, 255), active_joystick)
		screen.blit(js_name, (x, y))
