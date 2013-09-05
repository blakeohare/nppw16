
class DialogScene:
	def __init__(self, bg, dialogId, slightDelay, storyMode=False, forceArrow=False):
		self.next = self
		self.flags = ''
		self.bg = bg
		self.storyMode = storyMode
		self.forceArrow = forceArrow
		player = bg.player
		if player != None:
			player.moving = False
			player.lastDirection = 'left'
		self.delayCounter = 45 if slightDelay else 0
		self.stanzas = DIALOGS[dialogId]
		self.stanzaIndex = 0
		self.textCursor = 0
		self.showLines = []
		self.blink = False
		
		
		 # The epitome of a PyWeek hack
		self.generalLoc = None
		if len(dialogId) == 2 and dialogId[0] == 'T':
			self.generalLoc = (4 * 16, 6 * 16)
	
	def processInput(self, events, pressed):
		if self.blink:
			for event in events:
				if event.down and event.action in ('A', 'B', 'start'):
					self.stanzaIndex += 1
					self.textCursor = 0
		else:
			if pressed['A'] or pressed['B'] or pressed['start']:
				if self.delayCounter < 0:
					self.textCursor += 1.2
		
	
	def update(self):
		self.delayCounter -= 1
		if self.stanzaIndex >= len(self.stanzas):
			self.next = self.bg
			self.bg.next = self.bg
			#clearTextCache(255, 255, 255) # so much clutter
		else:
			self.activeStanza = self.stanzas[self.stanzaIndex]
			rawLines = '\n'.join(self.activeStanza)
			self.blink = False
			cursor = int(self.textCursor)
			if cursor >= len(rawLines):
				self.blink = True 
			else:
				rawLines = rawLines[:cursor]
			showLinesStr = rawLines.split('\n')
			showLines = []
			for line in showLinesStr:
				if len(line) > 0:
					showLines.append(getText((255, 255, 255), line))
			self.showLines = showLines
		
		if self.delayCounter < 0:
			self.textCursor += 0.3
	
	def render(self, screen, rc):
		self.bg.render(screen, rc)
		
		if self.delayCounter > 0: return
		
		if self.generalLoc != None:
			path = 'tiles/screen-static/screen' + ('', '1', '2', '3')[(rc // 4) & 3] + '.png'
			screen.blit(getImage(path), self.generalLoc)
		
		if not self.storyMode:
			drawBox(screen, 16, 16, 28, 9)
		x = 32
		y = 32
		space = 8
		if self.storyMode:
			y += 16 * 7
			space = 16
		
		startY = y
		for line in self.showLines:
			screen.blit(line, (x, y))
			y += space
		if self.blink and ((rc // 7) & 1) == 0:
			pos = (256 - 40, startY + space * 4)
			if not self.forceArrow and self.stanzaIndex == len(self.stanzas) - 1:
				pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos[0], pos[1], 8, 8))
			else:
				screen.blit(getText((255, 255, 255), '^'), pos)