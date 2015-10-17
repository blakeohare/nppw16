class VolcanoCoreActivation(SpecialLevelStuff):
	def __init__(self, scene, id):
		SpecialLevelStuff.__init__(self, scene)
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
		self.warpBack = False
		
	def update(self):
		
		player = self.scene.player
		tx = player.x // 16
		ty = player.y // 16
		
		if tx == self.spotX and abs(ty - self.spotY) < 2 and not self.done:
			self.doLavaSequence(False)
		
		self.freeze = False
		self.shakeScreen = False
		self.scene.player.sprinkle = False
		
		if self.sequenceCounter >= 0:
			SPRINKLE = 30 # player sprinkles mix
			SHAKE = 60 # screenshakes 
			RISE_RATE = 30 # this happens 3 times
			
			self.freeze = True
			sc = self.sequenceCounter
			if sc < SPRINKLE:
				self.scene.player.sprinkle = True
				if sc == 0:
					playNoise('sprinkle_lava_packet')
				progress = 1.0 * sc / SPRINKLE
			else:
				sc -= SPRINKLE
				if sc < SHAKE:
					if sc == 0:
						playNoise('screen_shaking')
					self.shakeScreen = (sc & 1) == 0
					
				else:
					sc -= SHAKE
					if sc < RISE_RATE:
						if sc == 0:
							playNoise('lava_rise')
						self.lavaLevel = 1
					else:
						sc -= RISE_RATE
						if sc < RISE_RATE:
							if sc == 0:
								playNoise('lava_rise')
							self.lavaLevel = 2
						else:
							sc -= RISE_RATE
							self.lavaLevel = 3
							if sc < RISE_RATE:
								if sc == 0:
									playNoise('lava_rise')
							else:
								self.freeze = False
								if self.warpBack:
									self.scene.next = VolcanoCompleteScene(self.scene, self.context)
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
			
		
		complete = self.context.volcanoA and self.context.volcanoB and self.context.volcanoC
		
		if not complete:
			if self.id == 1:
				self.context.volcanoA = True
			elif self.id == 2:
				self.context.volcanoB = True
			elif self.id == 3:
				self.context.volcanoC = True
			
			complete = self.context.volcanoA and self.context.volcanoB and self.context.volcanoC
			if complete:
				self.warpBack = True
			