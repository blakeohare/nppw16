# TODO: intro slide show

class IntroScene:
	def __init__(self):
		self.flags = ''
		self.next = self
	
	def processInput(self, events, pressedKeys):
		pass 
	
	def update(self):
		self.next = self.getStartScene()
	
	def render(self, screen, rc):
		pass
	
	def getStartScene(self):
		if os.path.exists('fast_start.txt'):
			c = open('fast_start.txt', 'rt')
			t = c.read().split('\n')
			c.close()
			i = 0
			ignore = False
			level = None
			x = 2
			y = 2
			flags = []
			for line in t:
				line = trim(line.split('#')[0])
				if len(line) > 0:
					i += 1
					if i == 1:
						if line == 'IGNORE':
							ignore = True
							break
						level = line
					elif i == 2:
						parts = line.split(',')
						x = int(trim(parts[0]))
						y = int(trim(parts[1]))
					else:
						flags.append(trim(line).lower())
			
			if not ignore:
				c = Context()
				for flag in flags:
					if flag == 'gravity':
						c.gravity = True
					elif flag == 'volcano1':
						c.volcanoA = True
					elif flag == 'volcano2':
						c.volcanoB = True
					elif flag == 'volcano3':
						c.volcanoC = True
					elif flag == 'water1':
						c.balloonA = True
					elif flag == 'water2':
						c.balloonB = True
					elif flag == 'water3':
						c.balloonC = True
				
				return PlayScene(level, x, y, c)
				
		return PlayScene('ship_1', 8, 9, Context())