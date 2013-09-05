class ShipTransmission(SpecialLevelStuff):
	def __init__(self, scene):
		SpecialLevelStuff.__init__(self, scene)
		self.hasUpdate = True
	
	def update(self):
		
		ctx = self.context
		if not ctx.gravity:
			if not ctx.transmission1:
				self.scene.triggerDialog('T1', True)
				ctx.transmission1 = True
		elif not (ctx.volcanoA and ctx.volcanoB and ctx.volcanoC):
			if not ctx.transmission2:
				self.scene.triggerDialog('T2', True)
				ctx.transmission2 = True
		elif not (ctx.balloonA and ctx.balloonB and ctx.balloonC):
			if not ctx.transmission3:
				self.scene.triggerDialog('T3', True)
				ctx.transmission3 = True
		else:
			if not ctx.transmission4:
				self.scene.triggerDialog('T4', True)
				ctx.transmission4 = True
	