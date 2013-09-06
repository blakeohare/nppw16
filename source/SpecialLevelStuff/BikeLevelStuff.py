class BikeLevelStuff(SpecialLevelStuff):
	def __init__(self, scene):
		SpecialLevelStuff.__init__(self, scene)
		self.hasUpdate = True
	
	def update(self):
		scene = self.scene
		player = scene.player
		if player.x > (scene.cols - 1) * 16: # one less because you can't technically go off screen
			scene.next = VictorySequenceScene(scene)
			