# Add maps to this list to alter what background they'll have

CAVE_BG = [
	'grav_ascent',
	'grav_core',
	'grav_descent',
	'grav_descent_secret'
]

STARS_BG = [
	'rope_test',
	'ship_1'
]





##########################################

_bg = {}
for cbg in CAVE_BG:
	_bg[cbg] = 'cave'
for sbg in STARS_BG:
	_bg[sbg] = 'stars'


def getBackground(level):
	level = level.split('.')[0]
	return _bg.get(level, 'sky')