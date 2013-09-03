
class GravityAscentExit(SpecialLevelStuff):
	def __init__(self, scene):
		SpecialLevelStuff.__init__(self, scene)
		self.hasDoorTrigger = True
	
	def doorTrigger(self, doorId):
		if doorId == 'XXXXX':
			self.scene.next = PlayScene('ship_1', 8, 8, self.scene.context)
			return None
		return doorId
