RISE_SPEED = 1
WAIT_INTERVAL = 30 * 4

class LavaMonsterAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.counter = 0
		self.mode = 'wait' # { wait | rise | shoot | fall }
		self.mouthOpen = False
		
	
	def doStuff(self, scene):
		self.counter += 1
		self.mouthOpen = False
		faceLeft = scene.player.x < self.sprite.x
		self.sprite.lastDirection = 'left' if faceLeft else 'right'
		if self.mode == 'wait':
			if self.counter == WAIT_INTERVAL:
				self.counter = 0
				self.mode = 'rise'
		elif self.mode == 'rise':
			if self.counter == 16:
				self.mode = 'shoot'
				self.counter = 0
			self.sprite.dy = -1
		elif self.mode == 'shoot':
			if self.counter == 60:
				self.mode = 'fall'
				self.counter = 0
			if self.counter == 7:
				self.createFireBall()
			if self.counter > 0 and self.counter < 14:
				self.mouthOpen = True
		
		elif self.mode == 'fall':
			if self.counter == 16:
				self.mode = 'wait'
				self.counter = 0
			self.sprite.dy = 1
		
		
	def createFireBall(self):
		fireball = Sprite('fireball', self.sprite.x, self.sprite.y)
		self.sprite.spawns = [fireball]
		