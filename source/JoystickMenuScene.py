class JoystickMenuScene:
	def __init__(self):
		self.next = self
		self.flags = ''
		self.options = ['None'] + get_joystick_manifest()
		self.index = 0 if (active_joystick == None) else (1 + joysticks_present[active_joystick])
		self.blink_counter = 0
	
	def processInput(self, events, pressedActions):
		for event in events:
			if event.down and self.blink_counter <= 0:
				if event.action == 'up':
					self.index -= 1
				elif event.action == 'down':
					self.index += 1
				elif event.action in ['A', 'B', 'start']:
					if self.index == 0:
						set_active_joystick(None)
						self.next = TitleScene()
					else:
						self.blink_counter = 30
				if self.index < 0:
					self.index = 0
				if self.index >= len(self.options):
					self.index = len(self.options) - 1
				
	
	def update(self):
		self.blink_counter -= 1
		if self.blink_counter == 1:
			self.next = JoystickConfigScreen(self.index - 1, self)
			self.blink_counter = 0
	
	def render(self, screen, rc):
		title = getText((255, 255, 0), "Joystick Selection")
		cursor = getText((255, 255, 255), ">")
		screen.fill((0, 0, 0))
		
		left = 32
		drawBox(screen, left - 16, 16, 30, (len(self.options) + 1) * 2 + 3)
		
		y = 32
		screen.blit(title, (32, y))
		y += 16
		index = 0
		for option in self.options:
			selected = False
			if index == self.index:
				screen.blit(cursor, (left, y))
				selected = True
			
			if not selected or self.blink_counter <= 0 or rc % 4 < 2:
				screen.blit(getText((255, 255, 255), option), (left + 16, y))
			index += 1
			y += 16
		
		