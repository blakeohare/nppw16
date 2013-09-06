def getSpecialLevelStuff(id, scene):
	if id == 'ship_1':
		return [ShipTransmission(scene)]
	if id == 'grav_core':
		return [GravityCorePlacement(scene)]
	if id == 'grav_ascent':
		return [GravityAscentExit(scene)]
	if id == 'volcano_1_core':
		return [VolcanoCoreActivation(scene, 1)]
	if id == 'volcano_2_core':
		return [VolcanoCoreActivation(scene, 2)]
	if id == 'volcano_3_core':
		return [VolcanoCoreActivation(scene, 3)]
	if id == 'balloon_2_overland':
		return [BalloonPopping(scene, 'water2')]
	if id == 'balloon_3_overland':
		return [BalloonPopping(scene, 'water3')]
	if id == 'main':
		return [BalloonPopping(scene, 'water1'),
			BalloonPopping(scene, 'lava1')]
	return []

class SpecialLevelStuff:
	def __init__(self, scene):
		self.scene = scene
		self.context = scene.context
		self.tiles = scene.tiles
		self.hasUpdate = False
		self.hasPostInit = False
		self.hasDoorTrigger = False
		
		# meh, hacks
		self.lavaLevel = 0
		self.shakeScreen = False
		self.freeze = False
	
	# override and return None if you want that door to do something special. 
	# The doorId will be post-swapped.
	def doorTrigger(self, doorId):
		return doorId