SONG_LOOKUP = {
	# name : (file, should loop?)
	'title': ('tensebranches', True),
	'intro': ('open_skies', True),
	'overworld': ('spacemachine', True),
}

SONG_BY_MAP = {
	'ship_1': 'overworld'
}

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