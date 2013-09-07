class BirdFeeder(SpecialLevelStuff):
	def __init__(self, scene):
		SpecialLevelStuff.__init__(self, scene)
		self.hasPostInit = True
		self.hasUpdate = True
		seeds = [(4,36),
			(11,30),
			(4,24),
			(11,18),
			(4,12),
			(11,6)]
		self.seedsLeft = len(seeds)
		for seed in seeds:
			scene.sprites.append(Sprite('seeds', seed[0] * 16 + 8, seed[1] * 16 + 7))
		
	def update(self):
		p = self.scene.player
		print(self.seedsLeft)
		
	def postInit(self):
		pass
		