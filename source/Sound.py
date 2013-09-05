SOUND_LOOKUP = {
	'raise_health': None,
	'head_bonk': None, # re-used when trying to move a menu cursor someplace where it cannot go.
	'password_enter_digit': None,
	'bad_password': None,
	'sprinkle_lava_packet': None,
	'screen_shaking': ('everythingfalls', 1.0),
	'fall_to_death': None,
	'lava_rise': None,
	'land_on_ground': None,
	'menu_select': None,
	'menu_move': None,
	'low_health': None,
	'get_hit': None,
	'raise_health': None,
	'jump': ('jump', 0.4),
	'swim': ('jump', 0.4), # maybe use a different sound?
	'pause_sound': None # *TEE KOO TEE KOO*
}

_sound_cache = {}
def playNoise(key):
	if not SOUND_ENABLED:
		return
	
	snd = _sound_cache.get(key)
	if snd == None:
		data = SOUND_LOOKUP.get(key)
		if data != None:
			filename = data[0]
			volumeRatio = data[1]
			path = 'sfx/' + filename + '.ogg'
			snd = pygame.mixer.Sound(path.replace('/', os.sep))
			snd.set_volume(volumeRatio)
			_sound_cache[key] = snd
	
	
	if snd != None:
		snd.play()
	