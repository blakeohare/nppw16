
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
	
		if tx == self.col and ty == self.row:
			self.done = True
			self.context.gravity = True
			self.addGDevice()
	
	def postInit(self):
		if self.context.gravity:
			self.addGDevice()
	
	def addGDevice(self):
		self.scene.sprites.append(Sprite('gravity_device', self.col * 16 + 8, self.row * 16 + 8))