class JoystickMenuScene:
	def __init__(self):
		self.next = self
		self.flags = ''
		self.options = ['None'] + get_joystick_manifest()
		self.index = 0 if (active_joystick == None) else (1 + joysticks_present[active_joystick])
	
	def processInput(self, events, pressedActions):
		for event in events:
			if event.down:
				if event.action == 'up':
					self.index -= 1
				elif event.action == 'down':
					self.index += 1
				elif event.action in ['A', 'B', 'start']:
					if self.index == 0:
						active_joystick = None
						self.next = TitleScene()
					else:
						self.next = JoystickConfigScreen(self.index - 1, self)
				if self.index < 0:
					self.index = 0
				if self.index >= len(self.options):
					self.index = len(self.options) - 1
				
	
	def update(self):
		pass
	
	def render(self, screen, rc):
		title = getText((255, 255, 0), "Joystick Selection")
		cursor = getText((255, 255, 255), ">")
		screen.fill((0, 0, 0))
		screen.blit(title, (32, 16))
		y = 32
		index = 0
		for option in self.options:
			if index == self.index:
				screen.blit(cursor, (16, y))
			screen.blit(getText((255, 255, 255), option), (32, y))
			index += 1
			y += 16
		
		