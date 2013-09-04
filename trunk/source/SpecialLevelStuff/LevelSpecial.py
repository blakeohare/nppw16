def getSpecialLevelStuff(id, scene):
	if id == 'ship_1':
		return [ShipTransmission(scene)]
	if id == 'grav_core':
		return [GravityCorePlacement(scene)]
	if id == 'grav_ascent':
		return [GravityAscentExit(scene)]
	return []

class SpecialLevelStuff:
	def __init__(self, scene):
		self.scene = scene
		self.context = scene.context
		self.tiles = scene.tiles
		self.hasUpdate = False
		self.hasPostInit = False
		self.hasDoorTrigger = False
	
	# override and return None if you want that door to do something special. 
	# The doorId will be post-swapped.
	def doorTrigger(self, doorId):
		return doorId