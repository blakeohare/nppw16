cred_BO = "BLAKE O'HARE"
cred_TB = "TED BURTON"
cred_SC = "STEVE CRAWFORD"
cred_LF = "LAURA FREER"
cred_CS = "CHRISTINE SANDQUIST"
cred_AM = "ANGEL MCLAUGHLIN"
cred_AC = "ADRIAN CLINE"



CREDITS = [
	('TEAM NERD PARADISE', []),
	('PROGRAMMING', [cred_BO]),
	('LEVEL DESIGN', [cred_TB, cred_SC, cred_LF]),
	('CHARACTER ART', [cred_CS]),
	('LEVEL ART', [cred_AM]),
	('MUSIC AND SFX', [cred_AC]),
	('DIALOG', [cred_LF]),
	('AND YOU!', ['FOR PLAYING', 'OR SOMETHING LIKE THAT']),
	('', ['THE END'])
]

class CreditsScene:
	def __init__(self):
		self.next = self
		self.flags = 'M'
		self.counter = 0
		
		images = []
		y = 0
		
		i = 0
		while i < len(CREDITS):
			images.append((getText(WHITE, CREDITS[i][0]), y))
			
			y += 16
			for person in CREDITS[i][1]:
				images.append((getText(WHITE, person), y))
				y += 8
			
			y += 64
			
			i += 1
		self.images = images
	
	def processInput(self, events, pressed):
		if self.counter > 900:
			for event in events:
				if event.down:
					if event.action in ('start', 'A', 'B'):
						self.next = TitleScene()
	
	def update(self):
		self.playMusic()
		self.counter += 1
	
	def render(self, screen, rc):
		screen.fill(BLACK)
		
		counter = min(self.counter, 892)
		
		for image in self.images:
			screen.blit(image[0], (64, image[1] - counter + 224))
	
	def playMusic(self):
		JUKEBOX.ensureSong('credits')