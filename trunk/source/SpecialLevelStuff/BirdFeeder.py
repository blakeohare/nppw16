class BirdFeeder(SpecialLevelStuff):
	def __init__(self, scene):
		SpecialLevelStuff.__init__(self, scene)
		self.hasPostInit = True
		self.hasUpdate = True
		self.counter = 0
		seeds = [(4,36),
			(11,30),
			(4,24),
			(11,18),
			(4,12),
			(11,6)]
		self.seedsLeft = len(seeds)
		for seed in seeds:
			scene.sprites.append(Sprite('seeds', seed[0] * 16 + 8, seed[1] * 16 + 7))
		
		scene.sprites.append(Sprite('rocketbike', 12 * 16 + 8, 39 * 16 + 8))
		
		self.closingShown = False
		
	def update(self):
		p = self.scene.player
		self.counter += 1
		
		if self.counter == 3:
			self.scene.next = DialogScene(self.scene, "Feeder1", False, False, False)
		
		if self.seedsLeft == 0 and not self.closingShown:
			self.scene.next = DialogScene(self.scene, "Feeder2", False, False, False)
			self.scene.sprites.append(Sprite('bird1', 8, 8))
			self.closingShown = True
		
		
		
	def postInit(self):
		pass
		