class GravityCorePlacement(SpecialLevelStuff):
	def __init__(self, scene):
		SpecialLevelStuff.__init__(self, scene)
		self.hasPostInit = True
		self.hasUpdate = True
		self.col = 11
		self.row = 9
		self.done = False
	
	def update(self):
		player = self.scene.player
		tx = int(player.x / 16)
		ty = int(player.y / 16)
	
		if tx == self.col and abs(ty - self.row) < 2 and not self.done:
			self.addGDevice(True)
	
	def postInit(self):
		if self.context.gravity:
			self.addGDevice()
	
	def addGDevice(self, showDialog=False):
		self.done = True
		self.context.gravity = True
		gd = Sprite('gravity_device', self.col * 16, self.row * 16)
		gd.floats = True
		self.scene.sprites.append(gd)
		if showDialog:
			self.scene.next = DialogScene(self.scene, 'GravityDone', True, False, False)
