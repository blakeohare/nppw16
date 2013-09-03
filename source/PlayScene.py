class PlayScene:
	def __init__(self, map, startCol, startRow, context):
		self.context = context
		self.next = self
		self.flags = ''
		levelname = map.split('.')[0]
		if not map.endswith('.map'):
			map += '.map'
		mapParser = MapParser(map)
		map = mapParser.parse()
		
		self.hasAtmosphere = False

		self.bg = getBackground(levelname)
		stars = legacyMap(lambda x:getImage('tiles/background/stars' + str(x) + '.png'), [1, 2, 3, 4, 5]) + ([None] * 10)
		stars *= 3
		random.shuffle(stars)
		self.stars = stars
		self.runCounter = 0
		self.runCounterValidFor = ':P'
		
		self.cols = map.width
		self.rows = map.height
		self.upper = map.upper
		self.lower = map.lower
		self.side = map.side
		
		self.tiles = makeGrid(self.cols, self.rows)
		
		self.doorSwaps = map.doorswaps
		
		doorTiles = []
		ladderTiles = {}
		lowerdoors = []
		y = self.rows - 1
		while y >= 0:
			x = 0
			while x < self.cols:
				
				t = Tile(self.lower[x][y], self.upper[x][y], x, y)
				self.tiles[x][y] = t
				if t.isDoor:
					doorTiles.append((str(x) + '|' + str(y), t))
					if self.side and y + 1 < self.rows:
						# add the tile below the door to the potential door tiles
						# the door list from the map parser will check for the tile below a door iff it's a tall door and is 
						# expecting to find it in this list. If not, then this gets safely ignored
						doorTiles.append((str(x) + '|' + str(y + 1), self.tiles[x][y + 1]))
						
				if t.isLadder:
					ladderTiles[str(x) + '|' + str(y)] = (x, y)
				x += 1
			y -= 1 # go backwards so doors can add lower neighbor
		
		for lk in ladderTiles.keys():
			coord = ladderTiles[lk]
			x = coord[0]
			y = coord[1]
			if y > 0:
				if ladderTiles.get(str(x) + "|" + str(y - 1)) == None:
					self.tiles[x][y].isTop = True
		
		doorLookup = {}
		for door in map.doors:
			xys = [(door.sx, door.sy)]
			if self.side:
				xys.append((door.sx, door.sy + 1))
			for xy in xys:
				doorLookup[str(xy[0]) + '|' + str(xy[1])] = door
		
		for doorTile in doorTiles:
			dk = doorTile[0]
			door = doorLookup.get(dk, None)
			if door != None:
				doorTile[1].door = door
				doorTile[1].collisions = []
				doorTile[1].solid = False
		
		self.cameraX = 0
		self.cameraY = 0
		
		self.player = Sprite('player_' + ('side' if self.side else 'over'), startCol * 16 + 8, startRow * 16 + 8)
		self.sprites = [self.player]
		
		for enemy in map.enemies:
			sprite = Sprite(enemy.id, enemy.col * 16 + 8, enemy.row * 16 + 8)
			sprite.isEnemy = True
			self.sprites.append(sprite)
		
		self.special = getSpecialLevelStuff(levelname, self)
		for special in self.special:
			if special.hasPostInit:
				special.postInit()
	
	def playersTile(self, offsetX=0, offsetY=0):
		if self.player == None: return None
		p = self.player
		tx = int(p.modelX / 16) + offsetX
		ty = int(p.modelY / 16) + offsetY
		if tx >= 0 and ty >= 0 and tx < self.cols and ty < self.rows:
			return self.tiles[tx][ty]
		return None
	
	def processInput(self, events, pressed):
		if self.side:
			dx = 0
			dy = 0
			running = False
			if self.context.gravity:
				if pressed['B']:
					running = True
					v = 5
				else:
					v = 3
			else:
				v = 2.5
				
			if pressed['left']:
				dx = -v
				if running and self.runCounterValidFor == 'left':
					self.runCounter += 1
				else:
					self.runCounter = 0
					self.runCounterValidFor = 'left'
			elif pressed['right']:
				dx = v
				if running and self.runCounterValidFor == 'right':
					self.runCounter += 1
				else:
					self.runCounter = 0
					self.runCounterValidFor = 'right'
			elif pressed['up']:
				pt = self.playersTile()
				if pt != None and pt.isLadder:
					self.player.cling = True
					#self.player.onGround = False
					self.player.ladderDY = -2
			elif pressed['down']:
				pt = self.playersTile()
				if pt != None and pt.isLadder:
					self.player.ladderDY = 2
				else:
					pt = self.playersTile(0, 1)
					if pt != None and pt.isLadder:
						self.player.modelY += 8
						self.player.ladderDY = 2
						self.player.cling = True
			else:
				self.runCounter = 0
				self.runCounterValidFor = 'nothing'
				
			if self.player != None:
				self.player.dx = dx
			
			for event in events:
				if event.action == 'A':
					if event.down:
						pt = self.playersTile()
						if self.player.onGround or self.player.cling or (pt != None and pt.isWater):
							self.player.onGround = False
							self.player.cling = False
							self.player.ladderDY = 0
							if pt.isWater:
								self.player.vy += WATER_JUMPING_VY
							else:
								self.player.vy = JUMPING_VY
								if self.runCounter > 5 and self.context.gravity:
									self.player.vy = RUN_JUMPING_VY
								
					else:
						if self.player.vy < 0:
							self.player.vy = self.player.vy / 4.0 # maybe set to 0 instead?
							
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
		playerX = self.player.modelX
		playerY = self.player.modelY
		for sprite in self.sprites:
			sprite.update(self)
			if sprite.isEnemy and self.player != None:
				if sprite.isCollision(self.player):
					self.playerHit()
			
		player_tx = int(self.player.modelX / 16)
		player_ty = int(self.player.modelY / 16)
		activeTile = self.tiles[player_tx][player_ty]
		if activeTile.door != None:
			door = activeTile.door
			target = door.target
			swaps = self.doorSwaps.get(target)
			
			if swaps != None:
				ctx = self.context
				for swap in swaps:
					trigger = swap[0]
					if ((
						trigger == 'gravity' and ctx.gravity) or (
						trigger == 'lavaA' and ctx.volcanoA) or (
						trigger == 'lavaB' and ctx.volcanoB) or (
						trigger == 'lavaC' and ctx.volcanoC) or (
						trigger == 'waterA' and ctx.balloonA) or (
						trigger == 'waterB' and ctx.balloonB) or (
						trigger == 'waterC' and ctx.balloonC)):
						target = swap[1]
						break
			
			for special in self.special:
				if special.hasDoorTrigger:
					target = special.doorTrigger(target)
					break
			
			if target != None:
				self.next = PlayScene(target, door.tx, door.ty, self.context)
		
		for special in self.special:
			if special.hasUpdate:
				special.update()
	
	def playerHit(self):
		if self.player.blinkCounter < 0:
			self.player.hit()
	
	def isCollision(self, pLeft, pTop, pRight, pBottom):
		if pLeft < 0: return True
		if pTop < 0: return True
		tLeft = int(pLeft / 16)
		tRight = tLeft if (pRight == pLeft) else int(pRight / 16)
		tTop = int(pTop / 16)
		
		# potentially a bug
		# bottom row of sprite is technically top row of ground below. This intersection should be ignored.
		tBottom = int((pBottom - 3) / 16) 
		
		if tLeft < 0: return True
		if tTop < 0: return True
		if tRight >= self.cols: return True
		if tBottom >= self.rows: return True
		
		y = tTop
		while y <= tBottom:
			x = tLeft
			while x <= tRight:
				if self.tiles[x][y].solid:
					return True
				x += 1
			y += 1
		return False
	
	def renderOverlay(self, screen):
		pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 256, 8))
		screen.blit(getImage('misc/lives.png'), (0, 0))
		txt = getText((255, 255, 255), 'x' + str(self.context.lives))
		screen.blit(txt, (8, 0))
	
	def render(self, screen, rc):
		if self.bg == 'stars':
			screen.fill((0, 0, 0))
		elif self.bg == 'cave':
			pass
		else:
			screen.fill((0, 0, 40)) # sky
		
		colStart = 0
		colEnd = self.cols - 1
		
		rowStart = 0
		rowEnd = self.rows - 1
		
		offsetX = -(self.player.x - 128)
		offsetY = -(self.player.y - 112)
		
		if offsetX > 0: offsetX = 0
		if offsetY > 0: offsetY = 0
		
		right = -(self.cols * 16 - 256)
		if offsetX < right: offsetX = right
		
		bottom = -(self.rows * 16 - 224)
		if offsetY < bottom: offsetY = bottom
		
		if self.cols * 16 < 256:
			offsetX = (256 - self.cols * 16) // 2
		if self.rows * 16 < 224:
			offsetY = (224 - self.rows * 16) // 2
		
		cave = getImage('tiles/background/cave.png')
		starlen = len(self.stars)
		stars = self.stars
		counter = 0
		
		idealColStart = -int(offsetX / 16) - 1
		if idealColStart > colStart:
			colStart = idealColStart
		
		idealColEnd = colStart + 17
		if idealColEnd < colEnd:
			colEnd = idealColEnd
		
		idealRowStart = -int(offsetY / 16) - 1
		if idealRowStart > rowStart:
			rowStart = idealRowStart
		
		idealRowEnd = rowStart + 15
		if idealRowEnd < rowEnd:
			rowEnd = idealRowEnd
		
		row = rowStart
		while row <= rowEnd:
			col = colStart
			while col <= colEnd:
				counter += 1
				x = col * 16 + offsetX
				y = row * 16 + offsetY
				pt = (x, y)
				if self.bg == 'cave':
					screen.blit(cave, pt)
				elif self.bg == 'stars':
					bgimg = stars[(col + self.rows * row + row * row) % starlen]
					if bgimg != None:
						screen.blit(bgimg, pt)
				tile = self.lower[col][row]
				if tile != None:
					screen.blit(tile.getImage(rc), pt)
				tile = self.upper[col][row]
				if tile != None:
					screen.blit(tile.getImage(rc), pt)
				
				col += 1
			row += 1
		
		arc = rc // 4
		for sprite in self.sprites:
			sprite.render(self, screen, offsetX, offsetY, arc)
			
				
		self.renderOverlay(screen)