class SeedAutomation:
	def __init__(self, sprite):
		self.counter = 0
		self.sprite = sprite
		self.used = False
		
	def doStuff(self, scene):
		p = scene.player
		dx = p.x - self.sprite.x
		dy = p.y - self.sprite.y
		if dx * dx + dy * dy < 100 and not self.used:
			self.sprite.dead = True
			self.used = True
			scene.special[0].seedsLeft -= 1
			playNoise('raise_health')