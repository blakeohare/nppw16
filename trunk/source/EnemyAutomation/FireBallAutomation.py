FIREBALL_VELOCITY = 1.5


class FireBallAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		self.counter = 0
		self.startX = sprite.x
		self.startY = sprite.y
		self.goLeft = sprite.lastDirection == 'left'
		self.vx = -FIREBALL_VELOCITY
		self.vy = 0
	
	def doStuff(self, scene):
		if self.counter == 0:
			dx = scene.player.x - self.startX
			dy = scene.player.y - self.startY
			
			if dx == 0:
				dx = 1
							
			m = 1.0 * dy / dx
			if m > 1.0:
				m = 1.0
			elif m < -1.0:
				m = -1.0
			ang = math.atan(m)
			self.vx = FIREBALL_VELOCITY * math.cos(ang)
			self.vy = -FIREBALL_VELOCITY * math.sin(ang)
			if self.goLeft:
				self.vx *= -1
		else:
			if self.predictedX != self.sprite.x:
				self.sprite.dead
				
		self.sprite.dx += self.vx
		self.sprite.dy += self.vy
		
		self.predictedX = int(self.sprite.dx + self.sprite.modelX)
		
		if self.sprite.collidedWall:
			self.sprite.dead = True
		
				
			
			
		self.counter += 1