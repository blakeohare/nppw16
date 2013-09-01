class PlayScene:
	def __init__(self, map, startCol, startRow):
		self.next = self
		self.flags = ''
		if not map.endswith('.map'):
			map += '.map'
		mapParser = MapParser(map)
		map = mapParser.parse()
		
		self.cols = map.width
		self.rows = map.height
		self.upper = map.upper
		self.lower = map.lower
		self.side = map.side
		
		self.cameraX = 0
		self.cameraY = 0
		
		self.player = Sprite('player_' + ('over' if self.side else 'side'), startCol * 16 + 8, startRow * 16 + 8)
		self.sprites = [self.player]
		
	def processInput(self, events, pressed):
		if self.side:
			print("TODO: side scroller part")
			z = 1 / 0
		else:
			v = 3
			dx = 0
			dy = 0
			
			if pressed['left']:
				dx = -v
			elif pressed['right']:
				dx = v
				
			if pressed['up']:
				dy = -v
			elif pressed['down']:
				dy = v
				
			self.player.dx = dx
			self.player.dy = dy
	
	def update(self):
		for sprite in self.sprites:
			sprite.update(self)
	
	def render(self, screen, rc):
		screen.fill((0, 0, 0))
		
		left = self.player.x - 128
		top = self.player.y - 112
		
		rowStart = 0
		rowEnd = self.rows - 1
		
		colStart = 0
		colEnd = self.cols - 1
		
		offsetX = -(self.player.x - 128)
		offsetY = -(self.player.y - 112)
		
		if offsetX > 0: offsetX = 0
		if offsetY > 0: offsetY = 0
		
		right = self.cols * 16 - 256
		if offsetX > right: offsetX = right
		bottom = self.rows * 16 - 224
		if offsetY > bottom: offsetY = bottom
		
		row = rowStart
		while row <= rowEnd:
			col = colStart
			while col <= colEnd:
				
				tile = self.lower[col][row]
				if tile != None:
					screen.blit(tile.getImage(rc), (col * 16 + offsetX, row * 16 + offsetY))
				tile = self.upper[col][row]
				if tile != None:
					screen.blit(tile.getImage(rc), (col * 16 + offsetX, row * 16 + offsetY))
				
				
				col += 1
			row += 1
		
		for sprite in self.sprites:
			sprite.render(screen, offsetX, offsetY, rc)