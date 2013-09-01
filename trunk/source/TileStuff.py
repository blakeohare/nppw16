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
		