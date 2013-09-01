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
		
		self.sprites = []
		
	
	def processInput(self, events, pressed):
		pass
	
	def update(self):
		pass
	
	def render(self, screen, rc):
		
		
		screen.fill((255, 0, 0))