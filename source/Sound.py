# This maps sound IDs used in the code to actual file names.
# If entry is None, no sound will be played when that event is triggered
# Otherwise, entry is a tuple of the filename (without extension, sfx/ is assumed) followed by a normalization ratio.

SOUND_LOOKUP = {
	'head_bonk': None, # fairly sublte sound as it will also happen a lot. Re-used when trying to move a menu cursor someplace where it cannot go.
	'password_enter_digit': None, 
	'bad_password': None, # sad fanfare: "DOO DOOoooo"
	'sprinkle_lava_packet': None, # "chkhchkhchkchkh" no longer than 1 second
	'screen_shaking': ('everythingfalls', 1.0), # done. perfect.
	'fall_to_death': None, # fairly obvious
	'lava_rise': None, # firey "FWOOM" sound
	'land_on_ground': None, # subtle sound as it will happen a lot
	'menu_select': None, # positive sound
	'menu_move': None, # subtle
	'low_health': None, # annoying as hell, 5 high pitched beeps in quick succession
	'get_hit': None, # use megaman taking-damage sound as inspiration, if that's doable.
	'raise_health': None, # dwoooOOO (but short)
	'jump': ('jump', 0.4), 
	'swim': ('jump', 0.4), # maybe use a different sound?
	'pause_sound': None # "TEE KOO TEE KOO!"
}

# TODO:
# ID's to place in code:
# - lava roast
# - enemy explodes
# - subtle text character bloop
# - make sure all menus have menu_move sound wired


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
	