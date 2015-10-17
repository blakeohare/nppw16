
class BalloonPopping(SpecialLevelStuff):
	# ID's: water1, water2, water3, water4, lava1, lava2, lava3
	def __init__(self, scene, id):
		SpecialLevelStuff.__init__(self, scene)
		self.id = id
		self.scene = scene
		self.context = scene.context
		self.hasUpdate = True
		self.hasPostInit = True
		self.done = False
		
		self.balloonCoords = {}
		
		if id.startswith('water'):
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
			
			if self.id == 'water1' and ty > 18: return
			if self.id == 'water4' and ty < 18: return
			
			tile = self.balloonCoords.get((tx, ty), None)
			if tile != None:
				self.applyOverlayAndSaveContext(True, (tx + tile.primaryBalloonOffset[0], ty + tile.primaryBalloonOffset[1]))

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
		elif self.id == 'water4':
			if self.context.balloonD:
				self.applyOverlayAndSaveContext()
		elif self.id == 'lava1':
			if self.context.volcanoA:
				self.applyOverlayAndSaveContext()
		elif self.id == 'lava2':
			if self.context.volcanoB:
				self.applyOverlayAndSaveContext()
		elif self.id == 'lava3':
			if self.context.volcanoC:
				self.applyOverlayAndSaveContext()
	
	def applyOverlayAndSaveContext(self, showPop=False, balloonLoc=None):
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
		elif self.id == 'water4':
			self.context.balloonD = True
		
		self.done = True
		
		if showPop:
			playNoise('water_pop')
			original.sprites.append(Sprite('waterpop', balloonLoc[0] * 16 + 8, balloonLoc[1] * 16 + 8))
		
		
			if self.context.balloonA and self.context.balloonB and self.context.balloonC and self.context.balloonD:
				self.scene.next = DialogScene(self.scene, 'WaterDone', True, False, False)