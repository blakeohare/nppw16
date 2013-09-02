_tileStore = {}
def getTile(id):
	if len(_tileStore) == 0:
		initTileStore()
	
	return _tileStore.get(id)

def initTileStore():
	c = open('images/tiles/manifest.txt'.replace('/', os.sep), 'rt')
	t = c.read()
	c.close()
	
	for line in t.split('\n'):
		parts = trim(line.split('#')[0]).split('\t')
		if len(parts) == 3:
			id = trim(parts[0])
			flags = trim(parts[1])
			imagePaths = trim(parts[2]).split(',')
			
			tile = TileTemplate(id, flags, imagePaths)
			_tileStore[id] = tile
			
		
class TileTemplate:
	def __init__(self, id, flags, imagePaths):
		self.id = id
		self.solid = False
		for flag in flags:
			if flag == 'x':
				self.solid = True
		self.images = []
		for path in imagePaths:
			self.images.append(getImage('tiles/' + path))
		self.staticImage = None
		if len(self.images) == 1:
			self.staticImage = self.images[0]
		self.imageCount = len(self.images)
	
	def getImage(self, rc):
		img = self.staticImage
		if img == None:
			return self.images[(rc // 4) % self.imageCount]
		return img

class Tile:
	def __init__(self, lower, upper, col, row):
		self.templates = []
		if lower != None:
			self.templates.append(lower)
		if upper != None:
			self.templates.append(upper)
		
		self.collisions = []
		
		coveredA = False
		coveredB = False
		coveredC = False
		coveredD = False
		
		for t in self.templates:
			if t.solid:
				coveredA = True
				coveredB = True
				coveredC = True
				coveredD = True
			else:
				coveredA = coveredA or t.coveredA
				coveredB = coveredB or t.coveredB
				coveredC = coveredC or t.coveredC
				coveredD = coveredD or t.coveredD
		
		leftCovered = coveredA and coveredC
		rightCovered = coveredB and coveredD
		topCovered = coveredA and coveredB
		bottomCovered = coveredC and coveredD
		
		if leftCovered and rightCovered:
			self.collisions.append([0, 0, 2, 2])
			coveredA = False
			coveredB = False
			coveredC = False
			coveredD = False
		elif leftCovered:
			self.collisions.append([0, 0, 1, 2])
			coveredA = False
			coveredC = False
		elif rightCovered:
			self.collisions.append([1, 0, 1, 2])
			coveredB = False
			coveredD = False
		elif topCovered:
			self.collisions.append([0, 0, 2, 1])
			coveredA = False
			coveredB = False
		elif bottomCovered:
			self.collisions.append([0, 1, 2, 1])
			coveredC = False
			coveredD = False
		
		if coveredA:
			self.collisions.append([0, 0, 1, 1])
		if coveredB:
			self.collisions.append([1, 0, 1, 1])
		if coveredC:
			self.collisions.append([0, 1, 1, 1])
		if coveredD:
			self.collisions.append([1, 1, 1, 1])
		
		i = 0
		while i < len(self.collisions):
			c = self.collsions[i]
			c[0] = c[0] * 8 + col * 16
			c[1] = c[1] * 8 + row * 16
			c[2] = c[0] + c[2] * 8
			c[3] = c[1] + c[3] * 8
			self.collisions[i] = c
			i += 1
		