FULL_LIFE = 10
START_LIFE = 10
START_LIVES = 3

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Context:
	
	def __init__(self):
		self.lifemeter = START_LIFE
		self.lives = START_LIVES
		self.volcanoA = False
		self.volcanoB = False
		self.volcanoC = False
		self.balloonA = False
		self.balloonB = False
		self.balloonC = False
		self.gravity = False
		self.transmission1 = False
		self.transmission2 = False
		self.transmission3 = False
		self.transmission4 = False
		self.powerupsTaken = {}
	
	def convertToPassword(self):
		
		if self.balloonA or self.balloonB or self.balloonC:
			count = 3
		elif self.volcanoA or self.volcanoB or self.volcanoC:
			count = 2
		elif self.gravity:
			count = 1
		else:
			count = 0
		
		password = ''
		
		if count == 1:
			password = 'A'
		elif count == 2:
			password = 'B'
		elif count == 3:
			password = 'C'
		else:
			password = self.randomChar(ALPHABET[3:])
		
		if count >= 1:
			if self.gravity:
				password += self.randomChar(ALPHABET[:13])
			else:
				password += self.randomChar(ALPHABET[13:])
		else:
			password += self.randomChar(ALPHABET)
		
		if count >= 2:
			value = self.volcanoA + (self.volcanoB * 2) + (self.volcanoC * 4)
			letter = chr(ord('1') + value - 1)
			password += letter
		else:
			password += self.randomChar('0123456789')
		
		if count >= 3:
			value = self.balloonA + (self.balloonB * 2) + (self.balloonC * 4)
			letter = chr(ord('A') + value - 1)
			password += letter
		else:
			password += self.randomChar(ALPHABET)
		
		return password
		
		
	# First letter:
	# A - 2nd letter is password, 3rd and 4th are random
	# B - 2nd and 3rd letter are password, 4th is random
	# C - All 3 are used
	# D+ - password is random, no state
	
	# Second letter when not random
	# <= M - gravity is on
	# >= N - gravity is off
	
	# Third letter when not random
	# 1 - volcanos 1, 0, 0
	# 2 - volcanos 0, 1, 0
	# 3 - volcanos 1, 1, 0
	# 4 - volcanos 0, 0, 1
	# 5 - volcanos 1, 0, 1
	# 6 - volcanos 0, 1, 1
	# 7 - volcanos 1, 1, 1
	# >= 8 - volcanos 0, 0, 0
	
	# Fourth letter when not random
	# same pattern for volcanos, but for water, also uses letters instead of numbers
	
	def randomChar(self, characters):
		return characters[int(random.random() * len(characters))]
	
	def enforceLetter(self, letter):
		letter = letter.upper()
		if ord(letter) < ord('A'):
			return 'A'
		if ord(letter) > ord('Z'):
			return 'Z'
		return letter
	
	def enforceNumber(self, char):
		if ord(char) < ord('0'):
			return '0'
		if ord(char) > ord('9'):
			return '9'
		return char
	
	def convertFromPassword(self, password):
		p1 = self.enforceLetter(password[0])
		p2 = self.enforceLetter(password[1])
		p3 = self.enforceLetter(password[2])
		p4 = self.enforceLetter(password[3])
		
		if p1 in 'ABC':
			if ord(p2) <= ord('M'):
				self.gravity = True
		
		if p1 in 'BC':
			value = ord(p3) - ord('1') + 1
			self.volcanoA = (value & 1) != 0
			self.volcanoB = (value & 2) != 0
			self.volcanoC = (value & 4) != 0
		
		if p1 == 'C':
			value = ord(p4) - ord('A') + 1
			self.balloonA = (value & 1) != 0
			self.balloonB = (value & 2) != 0
			self.balloonC = (value & 4) != 0
		
		self.lifemeter = START_LIFE
		self.lives = START_LIVES
		
	def adjustHealth(self, scene, amount):
		self.lifemeter += amount
		if self.lifemeter <= 0:
			self.lifemeter = 0
			scene.next = DeathOverrideScene(scene, 'collapse')
		else:
			if amount < 0:
				if self.lifemeter < 4:
					playNoise('low_health')
				else:
					playNoise('get_hit')
			else:
				playNoise('raise_health')
		
		if self.lifemeter > 10:
			self.lifemeter = 10
			