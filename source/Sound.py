# This maps sound IDs used in the code to actual file names.
# If entry is None, no sound will be played when that event is triggered
# Otherwise, entry is a tuple of the filename (without extension, sfx/ is assumed) followed by a normalization ratio.

SOUND_LOOKUP = {
	'head_bonk': ('head_bonk',1.0), # fairly sublte sound as it will also happen a lot. Re-used when trying to move a menu cursor someplace where it cannot go.
	'password_enter_digit':('password_digit_enter',1.0), 
	'bad_password': ('bad_password',1.0), # sad fanfare: "DOO DOOoooo"
	'sprinkle_lava_packet': ('sprinkle_lava',1.0), # "chkhchkhchkchkh" no longer than 1 second
	'screen_shaking': ('everythingfalls', 1.0), # done. perfect.
	'fall_to_death': ('fall_to_death',1.0), # fairly obvious
	'lava_rise': ('crash', 1.0),
	'land_on_ground': ('land_on_ground',0.5), # subtle sound as it will happen a lot
	
	# TODO(Blake): make sure these are hooked up in all menus
	'menu_select': ('menuhigh', 6.0), # positive sound
	'menu_move': ('menulow', 4.0), # subtle
	
	'low_health': ('low_health',1.0), # annoying as hell, 5 high pitched beeps in quick succession
	'get_hit': ('get_hit',1.0), # use megaman taking-damage sound as inspiration, if that's doable.
	'raise_health': ('raise_health',1.0), # dwoooOOO (but short)
	'jump': ('jump', 0.4), 
	'swim': ('jump', 0.4), # maybe use a different sound?
	'pause_sound': ('pause_sound',1.0), # "TEE KOO TEE KOO!"
	'lava_roast': ('lava_roast',1.0), # player dies by lava
	'text_char': ('text_char', 0.3), # subtle text character bloop
	'lazor': ('lazor',1.0), # player shoots lazor
	
	# TODO(Blake): The following are not hooked in by the code yet
	'enemy_dies': ('enemy_dies',1.0), # after shooting it
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
	