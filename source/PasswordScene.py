PASSWORD_BLOCK = [
	'123456789',
	'0ABCDEFGH',
	'IJKLMNOPQ',
	'RSTUVWXYZ']

class PasswordScene:
	def __init__(self):
		self.next = self
		self.flags = ''
		self.row = 0
		self.col = 0
		self.blinkCounter = 0
		self.current = ''
	
	def processInput(self, events, pressed):
		width = len(PASSWORD_BLOCK[0])
		height = len(PASSWORD_BLOCK)
		
		for event in events:
			dx = 0
			dy = 0
			if event.down:
				if event.action == 'up':
					dy -= 1
				elif event.action == 'down':
					dy += 1
				elif event.action == 'left':
					dx -= 1
				elif event.action == 'right':
					dx += 1
				elif event.action in ('A', 'start'):
					if self.row == 4 and self.col >= 5:
						self.next = TitleScene()
					else:
						if self.row == 4:
							self.tryCommit()
						else:
							if len(self.current) == 4:
								playNoise('head_bonk')
							else:
								if self.row < 4:
									if len(self.current) == 4:
										playNoise('head_bonk')
									else:
										playNoise('password_enter_digit')
										self.current += PASSWORD_BLOCK[self.row][self.col]
								
				elif event.action == 'B':
					if len(self.current) > 0:
						self.current = self.current[:-1]
					else:
						playNoise('head_bonk')
			
			newCol = self.col + dx
			newRow = self.row + dy
			if dx != 0 or dy != 0:
				bonk = False
				if self.row == 4:
					if dy == -1:
						pass #allow
					elif dy == 1:
						bonk = True
					elif dx == -1:
						if self.col >= 5:
							newCol = 0
						else:
							bonk = True
					elif dx == 1:
						if self.col < 5:
							newCol = 6
						else:
							self.bonk = True
				else:
					if newCol < 0 or newRow < 0:
						self.bonk = True
					if newCol >= width:
						self.bonk = True
				if not bonk:
					self.col = newCol
					self.row = newRow
					playNoise('menu_beep')
				else:
					playNoise('head_bonk')
	
	def tryCommit(self):
		if len(self.current) != 4:
			playNoise('bad_password')
			return
		for i in (0, 1, 3):
			if not (self.current[i] in ALPHABET):
				print(i)
				playNoise('bad_password')
				return
		
		if not (self.current[2] in '0123456789'):
			print('1')
			playNoise('bad_password')
			return
		
		context = Context()
		context.convertFromPassword(self.current)
		
		self.next = PlayScene('ship_1', 8, 9, context)
		
				
	
	def update(self):
		self.blinkCounter += 1

	def getCoord(self, col, row):
		return (8 + col * 24 + 24, 64 + row * 16)
	
	def render(self, screen, rc):
		screen.fill((0, 0, 0))
		
		hleft = 48
		drawBox(screen, hleft, 0, 18, 5)
		header = getText(WHITE, "Password Entry")
		screen.blit(header, (hleft + 16, 16))
		
		gleft = 8
		gtop = 48
		drawBox(screen, gleft, gtop, 30, 13)
		pb = PASSWORD_BLOCK
		blink = self.blinkCounter % 16 < 8
		height = len(pb)
		width = len(pb[0])
		y = 0
		while y < height:
			x = 0
			while x < width:
				letter = getText(WHITE, pb[y][x])
				c = self.getCoord(x, y)
				screen.blit(letter, c) # (gleft + 24 + x * 24, gtop + 16 + y * 16)
				if self.col == x and self.row == y:
					if blink:
						screen.blit(getText(WHITE, '>'), (c[0] - 8, c[1]))
				x += 1
			y += 1
		
		x = 0
		y = 4
		px = gleft + 24 + x * 24
		py = gtop + 16 + y * 16
		screen.blit(getText(WHITE, "DONE"), (px, py))
		if self.row == 4 and self.col < 5 and blink:
			screen.blit(getText(WHITE, '>'), (px - 8, py))
		x = 6
		px = gleft + 24 + x * 24
		screen.blit(getText(WHITE, "CANCEL"), (px, py))
		if self.row == 4 and self.col >= 5 and blink:
			screen.blit(getText(WHITE, '>'), (px - 8, py))
		
		oleft = 88
		otop = 224 - 64
		drawBox(screen, oleft, otop, 8, 5)
		txt = getText(WHITE, self.current)
		screen.blit(txt, (oleft + 16, otop + 16))