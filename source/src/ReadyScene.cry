class ReadyScene:
	def __init__(self, previousScene, context):
		self.next = self
		self.flags = ''
		self.context = context
		self.startArgs = previousScene.startArgs
		self.counter = 0
		self.playscene = PlayScene(self.startArgs[0], self.startArgs[1], self.startArgs[2], self.context)
	
	def processInput(self, events, pressed):
		pass
	
	def update(self):
		self.playscene.playMusic()
		self.counter += 1
		if self.counter > 90:
			self.next = self.playscene
	
	def render(self, screen, rc):
		if self.counter < 21:
			screen.fill((0, 0, 0))
		else:
			self.playscene.render(screen, 0)
			txt = getText(WHITE, 'ready')
			if (rc % 8 < 4):
				screen.blit(txt, (112, 112))