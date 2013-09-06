class MapParser:
	def __init__(self, file):
		path = ('maps/' + file).replace('/', os.sep).replace('\\', os.sep)
		c = open(path, 'rt')
		t = c.read()
		c.close()
		values = {}
		for line in t.split('\n'):
			parts = line.split(':')
			if len(parts) < 2:
				continue
			
			key = trim(parts[0][1:])
			value = trim(':'.join(parts[1:]))
			values[key] = trim(value)
		self.values = values
	
	def parse(self):
		m = StemCell()
		m.width = int(self.values['width'])
		m.height = int(self.values['height'])
		m.side = self.values.get('view', 'side').lower() == 'side'
		m.upper = self.getTiles(self.values['upper'], m.width, m.height)
		m.lower = self.getTiles(self.values['lower'], m.width, m.height)
		m.doors = self.getDoors(self.values.get('doors', ''))
		m.enemies = self.getEnemies(self.values.get('enemies', ''))
		m.doorswaps = self.getDoorswaps(self.values.get('doorswaps', ''))
		m.overlayTriggers = self.getOverlayTriggers(self.values.get('overlay', ''))
		m.powerups = self.getPowerups(self.values.get('powerups', ''))
		return m
	
	def getPowerups(self, sv):
		sv = trim(sv)
		if len(sv) == 0:
			return []

		output = []
		for item in sv.split(','):
			parts = item.split('|')
			pu = StemCell()
			pu.type = parts[0]
			pu.id = parts[1]
			pu.col = int(parts[2])
			pu.row = int(parts[3])
			output.append(pu)
		return output
		
	def getOverlayTriggers(self, strValue):
		strValue = trim(strValue)
		if len(strValue) == 0:
			return {}
		
		output = {}
		items = strValue.split(',')
		for item in items:
			parts = item.split('|')
		
			if len(parts) == 2:
				output[trim(parts[0])] = trim(parts[1])
		
		return output
	
	# door swap output format:
	# { original ID => List[ Pair<trigger, swapped ID> ] }
	def getDoorswaps(self, strValue):
		strValue = trim(strValue)
		if len(strValue) == 0:
			return {}
		swaps = {}
		for swap in strValue.split(','):
			parts = swap.split('|')
			trigger = trim(parts[0])
			original = trim(parts[1])
			swapped = trim(parts[2])
			
			swaps[original] = swaps.get(original, [])
			swaps[original].append((trigger, swapped))
		return swaps
		
	
	def getEnemies(self, enemyString):
		enemyString = trim(enemyString)
		if len(enemyString) == 0:
			return []
		enemies = []
		for value in enemyString.split(','):
			parts = value.split('|')
			id = parts[0]
			col = int(parts[1])
			row = int(parts[2])
			e = StemCell()
			e.id = id
			e.col = col
			e.row = row
			enemies.append(e)
		return enemies
	
	def getDoors(self, doorString):
		doorString = trim(doorString)
		if len(doorString) == 0:
			return []
		doors = []
		for door in doorString.split(','):
			door = door.split('|')
			d = StemCell()
			d.target = door[0]
			d.sx = int(door[1])
			d.sy = int(door[2])
			d.tx = int(door[3])
			d.ty = int(door[4])
			doors.append(d)
		return doors
		
	def getTiles(self, ids, width, height):
		output = []
		for id in map(trim, ids.split(',')):
			if id == '':
				output.append(None)
			else:
				output.append(getTile(id))
		
		grid = makeGrid(width, height)
		y = 0
		index = 0
		while y < height:
			x = 0
			while x < width:
				grid[x][y] = output[index]
				index += 1
				x += 1
			y += 1
		return grid