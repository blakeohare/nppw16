
class BalloonPopping(SpecialLevelStuff):
	# ID's: water1, water2, water3
	def __init__(self, scene, id):
		SpecialLevelStuff.__init__(self, scene)
		self.id = id
		self.scene = scene
		self.context = scene.context
		self.hasUpdate = True
		self.hasPostInit = True
		self.done = False
		
		self.balloonCoords = {}
		
		rows = scene.rows
		cols = scene.cols
		y = 0
		while y < rows:
			x = 0
			while x < cols:
				if scene.tiles[x][y].isBalloon:
					self.balloonCoords[(x, y)] = scene.tiles[x][y]
				x += 1
			y += 1
		
	def update(self):		
		if not self.done:
			player = self.scene.player
			tx = player.x // 16
			ty = player.y // 16
			
			tile = self.balloonCoords.get((tx, ty), None)
			if tile != None:
				self.applyOverlayAndSaveContext()

	def postInit(self):
		if self.id == 'water1':
			if self.context.balloonA:
				self.applyOverlayAndSaveContext()
		elif self.id == 'water2':
			if self.context.balloonB:
				self.applyOverlayAndSaveContext()
		elif self.id == 'water3':
			if self.context.balloonC:
				self.applyOverlayAndSaveContext()
	
	def applyOverlayAndSaveContext(self):
		if self.done:
			return
		
		overlayMapName = self.scene.overlayTriggers[self.id] # Go ahead and crash if not present. Game is busted at this point anyway.
		
		overlay = PlayScene(overlayMapName, 0, 0, Context())
		original = self.scene
		
		width = min(original.cols, original.cols)
		height = min(original.rows, original.rows)
		grid = original.tiles
		overlayTiles = overlay.tiles
		y = 0
		while y < height:
			x = 0
			while x < width:
				if len(overlay.tiles[x][y].originalTemplates) > 0:
					templates = grid[x][y].originalTemplates + overlay.tiles[x][y].originalTemplates
					grid[x][y] = Tile(templates, x, y)
				x += 1
			y += 1
		
		
		if self.id == 'water1':
			self.context.balloonA = True
		elif self.id == 'water2':
			self.context.balloonB = True
		elif self.id == 'water3':
			self.context.balloonC = True
		
		self.done = True
		