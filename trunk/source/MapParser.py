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
		m.side = self.values['view'].lower() == 'side'
		m.upper = self.getTiles(self.values['upper'], m.width, m.height)
		m.lower = self.getTiles(self.values['lower'], m.width, m.height)
		return m
		
		
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