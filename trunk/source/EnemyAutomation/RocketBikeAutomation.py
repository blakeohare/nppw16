class RocketBikeAutomation:
	def __init__(self, sprite):
		self.counter = 0
		self.sprite = sprite
		self.used = False
		
	def doStuff(self, scene):
		p = scene.player
		dx = p.x - self.sprite.x
		dy = p.y - self.sprite.y
		if dx * dx + dy * dy < 100:
			if scene.special[0].seedsLeft == 0:
				scene.next = PlayScene('bike_level', 8, 7, scene.context)