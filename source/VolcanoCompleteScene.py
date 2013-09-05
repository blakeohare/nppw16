class VolcanoCompleteScene:
	def __init__(self, scene, context):
		self.next = self
		self.flags = ''
		self.bg = scene
		self.context = context
		self.counter = 0
		self.player = scene.player
	
	def processInput(self, events, pressed):
		pass
	
	def update(self):
		self.counter += 1
		if self.counter == 20:
			self.next = DialogScene(self, 'Volcano', False)
		
		if self.counter == 30:
			self.next = PlayScene('ship_1', 8, 9, self.context)
		
	def render(self, screen, rc):
		self.bg.render(screen, rc)
	