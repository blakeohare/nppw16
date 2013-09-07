SONG_LOOKUP = {
	# name : (file, should loop?)
	'title': ('tensebranches', True),
	'intro': ('open_skies', True),
	'overworld': ('open_skies', True),
	'ship': ('spacemachine', True),
	'credits': ('credits', True),
	'password': ('fluffytales', True),
	'volcano': ('lunacy', True),
	'bike': ('nopressure', True),
	'water': ('squirrels_can_swim', True),
	'gravity': ('deadlyacorns', True),
	'death': ('oopsdead', False),
	'gameover': ('fluffytales', True),
}

SONG_BY_MAP = {
	'ship_1': 'ship',
	
	'main': 'overworld',
	'balloon_2_overland': 'overworld',
	'balloon_3_overland': 'overworld',
	'bird_overland': 'overworld',
	'volcano_2_overland': 'overworld',
	'volcano_3_overland': 'overworld',
	
	'bike_level': 'bike',
	
	'exit_water_phase_locked': 'water',
	'exit_water_phase_unlocked': 'water',
	
	'grav_ascent': 'gravity',
	'grav_core': 'gravity',
	'grav_descent': 'gravity',
	'grav_descent_secret': 'gravity',
	'grav_gate': 'gravity',
	
	'lava_gate_2': 'volcano',
	'lava_gate_2_active': 'volcano',
	'lava_gate_3': 'volcano',
	'lava_gate_3_active': 'volcano',
	'volcano_1_ascent': 'volcano',
	'volcano_1_core': 'volcano',
	'volcano_1_descent': 'volcano',
	'volcano_2_core': 'volcano',
	'volcano_2_lower_ascent': 'volcano',
	'volcano_2_lower_descent': 'volcano',
	'volcano_2_upper_ascent': 'volcano',
	'volcano_2_upper_descent': 'volcano',
	'volcano_2_upper_secret': 'volcano',
	'volcano_3_bottom': 'volcano',
	'volcano_3_core': 'volcano',
	'volcano_3_middle': 'volcano',
	'volcano_3_secret': 'volcano',
	'volcano_3_top': 'volcano',
	
	'water_gate_1_locked': 'water',
	'water_gate_1_unlocked': 'water',
	
	'rope_test': 'gravity',
	
	'birdfeeder': 'gravity',
	
	'section_3_gate': 'gravity',
	'section_3_gate_active': 'gravity',
	'wlink_A1': 'gravity',
	'wlink_A2': 'gravity',
	'wlink_A3': 'gravity',
	'wlink_A4': 'gravity',
	
	'wlink_B_nowater': 'water',
	'wlink_B_somewater': 'water',
	'wlink_B_allwater': 'water',
	
	'wlink_D1_nowater': 'water',
	'wlink_D1_water': 'water',
	'wlink_D2_nowater': 'water',
	'wlink_D2_water': 'water',
	'wlink_D3_nowater': 'water',
	'wlink_D3_water': 'water',
	
	'wlink_E1_nowater': 'water',
	'wlink_E1_water': 'water',
	'wlink_E2': 'water',
	'wlink_E3': 'water',
}

for file in os.listdir('maps'):
	if file.endswith('.map'):
		if 'overlay' in file:
			pass
		else:
			song = SONG_BY_MAP.get(file.split('.')[0])
			if song == None:
				print("ERROR: no song assigned to map file: " + file)



class JukeBox:
	def __init__(self):
		self.currentSong = None
		self.actuallyPlaying = False
	
	def ensureSong(self, id):
		if not SOUND_ENABLED:
			return
		
		if self.currentSong != id:
			if self.currentSong != None and self.actuallyPlaying:
				pygame.mixer.music.stop()
			song = SONG_LOOKUP.get(id)
			if song != None:
				file = song[0]
				loop = song[1]
				path = 'music/' + song[0] + '.ogg'
				pygame.mixer.music.load(path.replace('/', os.sep))
				pygame.mixer.music.play(-1 if loop else 0)
				self.actuallyPlaying = True
			else:
				self.actuallyPlaying = False
			
			self.currentSong = id
	
	def playSongForLevelMaybe(self, id):
		song = SONG_BY_MAP.get(id)
		if song != None:
			self.ensureSong(song)
	
JUKEBOX = JukeBox()