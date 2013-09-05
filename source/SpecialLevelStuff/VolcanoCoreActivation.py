class VolcanoCoreActivation(SpecialLevelStuff):
	def __init__(self, scene, id):
		SpecialLevelStuff
		self.id = id
		self.scene = scene
		self.context = scene.context
		self.hasUpdate = True
		self.hasPostInit = True
		self.spotX = 11
		self.spotY = 9
		self.sequenceCounter = -1
		self.done = False
		self.lavaLevel = 0
		self.shakeScreen = False
		self.freeze = False
		
	def update(self):
		
		player = self.scene.player
		tx = player.x // 16
		ty = player.y // 16
		
		if tx == self.spotX and abs(ty - self.spotY) < 2 and not self.done:
			print("This line was hit B")
			self.doLavaSequence(False)
		
		self.freeze = False
		self.shakeScreen = False
		if self.sequenceCounter >= 0:
			SPRINKLE = 30 # player sprinkles mix
			SHAKE = 60 # screenshakes 
			RISE_RATE = 30 # this happens 3 times
			
			self.freeze = True
			sc = self.sequenceCounter
			if sc < SPRINKLE:
				if sc == 0:
					playNoise('sprinkle_laval_packet')
				progress = 1.0 * sc / SPRINKLE
				print("SPRINKLE")
			else:
				sc -= SPRINKLE
				if sc < SHAKE:
					print("SHAKE")
					if sc == 0:
						playNoise('screen_shaking')
					self.shakeScreen = (sc & 1) == 0
					
				else:
					sc -= SHAKE
					if sc < RISE_RATE:
						print("RISE A")
						if sc == 0:
							playNoise('lava_rise')
						pass # level A
						self.lavaLevel = 1
					else:
						sc -= RISE_RATE
						if sc < RISE_RATE:
							print("RISE B")
							if sc == 0:
								playNoise('lava_rise')
							pass #level  B
							self.lavaLevel = 2
						else:
							sc -= RISE_RATE
							self.lavaLevel = 3
							if sc < RISE_RATE:
								print("RISE C")
								if sc == 0:
									playNoise('lava_rise')
								pass # level C
							else:
								
								print("DONE - level 3")
								self.freeze = False
			self.sequenceCounter += 1

	def postInit(self):
		isLavaOn = False
		if self.id == 1:
			isLavaOn = self.context.volcanoA
		elif self.id == 2:
			isLavaOn = self.context.volcanoB
		elif self.id == 3:
			isLavaOn = self.context.volcanoC
		
		if isLavaOn:
			self.doLavaSequence(True)
		
	
	def doLavaSequence(self, instant):
		self.done = True
		if instant:
			self.sequenceCounter = 9999999
		else:
			self.sequenceCounter = 0
		