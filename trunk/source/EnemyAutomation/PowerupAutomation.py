class PowerupAutomation:
	def __init__(self, sprite):
		self.sprite = sprite
		
	def doStuff(self, scene):
		player = scene.player
		
		for playerY in (player.y, player.y - 16):
			x = player.x
			y = playerY
			dx = self.sprite.x - x
			dy = self.sprite.y - y
			if dx * dx + dy * dy < 144:
				self.applyPowerup(scene.context)
	
	def applyPowerup(self, context):
		self.sprite.dead = True
		info = self.sprite.powerupInfo
		id = info.id
		type = info.type
		if id != None:
			context.powerupsTaken[id] = True
		if type == 'life_small':
			playNoise('raise_health')
			context.lifemeter += 2
			if context.lifemeter > 10:
				context.lifemeter = 10
		elif type == 'life_big':
			playNoise('raise_health')
			context.lifemeter = 10
		elif type == '1up':
			playNoise('1up')
			context.lives += 1
