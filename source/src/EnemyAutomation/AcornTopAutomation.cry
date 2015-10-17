ACORN_TOP_SPEED = 4.5

TRAIL = []

# this is the best I can come up with off the top of my head. I'm sure there's a faster way to create a parametric function of the acorn top path

ball = [0, 0]

waypoints = [
	[-1, 0],
	[-6, 0],
	[-6.6, -0.4],
	[-7, -1],
	[-6.6, -1.6],
	[-6, -2],
	[-1, -2],
	[-0.4, -1.6],
	[0, -1],
	[0, -.5]]

v = ACORN_TOP_SPEED + 0.0

i = 0
while i < len(waypoints):
	
	target = waypoints[i]
	tx = target[0] * 16.0
	ty = target[1] * 16.0
	
	done = False
	while not done:
		dx = tx - ball[0]
		dy = ty - ball[1]
		distance = (dx ** 2 + dy ** 2) ** .5
		if distance <= v:
			done = True
			TRAIL.append((tx, ty))
			ball = [tx, ty]
		else:
			dx *= v / distance
			dy *= v / distance
			ball[0] += dx
			ball[1] += dy
			TRAIL.append((int(10 * ball[0]) / 10.0, int(10 * ball[1]) / 10.0))
	i += 1


class AcornTopAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.trail = TRAIL[:]
		self.trailIndex = 0
		self.startX = sprite.modelX
		self.startY = sprite.modelY
		self.completed = False
	
	def setGoLeft(self, goLeft):
		self.goLeft = goLeft
		self.xSign = 1 if self.goLeft else -1
	
	def setGoUp(self, goUp):
		self.ySign = 1 if goUp else -1
	
	def doStuff(self, scene):
		if self.trailIndex < len(self.trail):
			
			rawX = self.trail[self.trailIndex][0]
			rawY = self.trail[self.trailIndex][1]
			
			rawX *= self.xSign
			rawY *= self.ySign
			
			targetX = self.startX + rawX
			targetY = self.startY + rawY
			
			dx = targetX - self.sprite.modelX
			dy = targetY - self.sprite.modelY
			
			self.sprite.dx = dx
			self.sprite.dy = dy
			
			self.trailIndex += 1
		else:
			if self.completed:
				self.sprite.dead = True
			self.completed = True
				