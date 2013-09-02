class JoystickConfigScreen:
	def __init__(self, js_index, bg):
		self.bg = bg
		self.bg.next = self.bg
		self.js_index = js_index
		self.next = self
		self.flags = ''
		self.buttons = 'left right up down A B start'.split(' ')
		self.phase = 0
		self.configs_taken = {}
		self.config = {}
	
	def processInput(self, events, pressed):
		pass
	
	def update(self):
		if self.phase < len(self.buttons):
			if self.do_poll():
				self.phase += 1
		
		if self.phase == len(self.buttons):
			name = joystick_instances[self.js_index].get_name()
			cached_joysticks[name] = self.config
			set_active_joystick(name)
			serialize_joystick_config()
			self.next = TitleScene()
	
	def do_poll(self):		
		button = self.buttons[self.phase]
		js = joystick_instances[self.js_index]
		
		for i in range(js.get_numbuttons()):
			if js.get_button(i):
				key = 'B' + str(i)
				if not self.configs_taken.get(key, False):
					self.configs_taken[key] = True
					self.config[button] = ('B', i)
					return True
		
		for i in range(js.get_numaxes()):
			value = js.get_axis(i)
			if value > 0.3:
				key = "A" + str(i) + '+'
				if not self.configs_taken.get(key, False):
					self.configs_taken[key] = True
					self.config[button] = ('A', i, True)
					return True
			elif value < -0.3:
				key = "A" + str(i) + '-'
				if not self.configs_taken.get(key, False):
					self.configs_taken[key] = True
					self.config[button] = ('A', i, False)
					return True
		
		for i in range(js.get_numhats()):
			value = js.get_hat(i)
			for j in (0, 1):
				if value[j] == 1:
					key = 'H' + str(i) + "|" + str(j) + "+"
					if not self.configs_taken.get(key, False):
						self.configs_taken[key] = True
						self.config[button] = ('H', i, j, True)
						return True
				elif value[j] == -1:
					key = 'H' + str(i) + "|" + str(j) + '-'
					if not self.configs_taken.get(key, False):
						self.configs_taken[key] = True
						self.config[button] = ('H', i, j, False)
						return True
		return False
	
	def render(self, screen, rc):
		self.bg.render(screen, rc)
		drawBox(screen, 40, 64, 20, 15)
		
		if self.phase < len(self.buttons):
			button = self.buttons[self.phase]
			txt = getText((255, 255, 255), "Press " + button)
			screen.blit(txt, (40 + 16, 64 + 16))
			img_name = button.lower()
			if ((rc // 6) % 2) == 0:
				img_name = 'none'
			screen.blit(getImage('misc/nes_' + img_name + '.png'), (40 + 16, 64 + 32))
			