CHASE_DISTANCE_TILES = 6

class MoonSquidAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.counter = 0
		self.goLeft = random.random() < .5
	
	def doStuff(self, scene):
		self.counter += 1
		player = scene.player
		sprite = self.sprite
		dx = player.x - sprite.x
		dy = player.y - sprite.y
		if dx * dx + dy * dy < (16 * CHASE_DISTANCE_TILES) ** 2:
			v = (math.sin(self.counter / 30.0 * 2 * 3.14159 / 2) + 1) / 1.5
			if dx == 0 and dy == 0:
				pass
			else:
				d = (dx * dx + dy * dy) ** .5
				dx *= v / d
				dy *= v / d
				sprite.dx = dx
				sprite.dy = dy
		else:
			if sprite.collidedWall:
				self.goLeft = not self.goLeft
			else:
				sprite.dx =  -1 if self.goLeft else 1