class AcornAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.countdown = int(random.random() * 5 * 30)
		self.mode = 'patrolling' # patrolling | throwing | baldpatrolling
		self.top = None
	
	def doStuff(self, scene):
		self.countdown -= 1
		walk = False
		if self.mode == 'patrolling':
			if self.countdown <= 0:
				self.mode = 'throwing'
				self.top = Sprite('acorntop', self.sprite.x, self.sprite.y)
				self.top.acorntopdir = self.sprite.lastDirection
				self.top.goLeft = self.top.acorntopdir == 'left'
				self.top.automation.body = self.sprite
				self.top.deleteWhenOffScreen = True
				self.top.ghost = True
				self.sprite.spawns = [self.top]
			else:
				walk = True
		elif self.mode == 'throwing':
			if self.top.dead:
				self.mode = 'baldpatrolling'
		elif self.mode == 'baldpatrolling':
			walk = True
		
		if walk:
			pass
			# TODO: walk back and forth, but don't fall off.

class AcornTopAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.countdown = 40
	
	def doStuff(self, scene):
		self.countdown -= 1
		if self.countdown == 0:
			self.goLeft = not self.goLeft
		
		# TODO: "loop" as it approaches 0 and then afterwards, go back to the sender in a straight line
		if self.goLeft:
			self.sprite.dx = -3
		else:
			self.sprite.dx = 3
		
				