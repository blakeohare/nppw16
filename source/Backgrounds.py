# Add maps to this list to alter what background they'll have

CAVE_BG = [
	'grav_ascent',
	'grav_core',
	'grav_descent',
	'grav_descent_secret',
	'grav_gate',
	'section_3_gate',
	'section_3_gate_active',
  'exit_water_phase_locked',
  'exit_water_phase_unlocked',
  'water_gate_1_locked',
  'water_gate_1_unlocked',
  'wlink_A1',
  'wlink_A2',
  'wlink_A3',
  'wlink_A4',
  'wlink_B_nowater',
  'wlink_B_somewater',
  'wlink_B_allwater',
  'wlink_D1_water',
  'wlink_D1_nowater',
  'wlink_D2_water',
  'wlink_D2_nowater',
  'wlink_D3_water',
  'wlink_D3_nowater',
  'wlink_E1_water',
  'wlink_E1_nowater',
  'wlink_E2',
  'wlink_E3',
  'bird_link',
]

VOLCANO_BG = [
	'volcano_1_ascent',
	'volcano_1_core',
	'volcano_1_core_active',
	'volcano_1_descent',
	'lava_gate_2',
	'lava_gate_2_active',
	'lava_gate_3',
	'lava_gate_3_active',
	'volcano_2_core',
	'volcano_2_lower_ascent',
	'volcano_2_lower_descent',
	'volcano_2_upper_ascent',
	'volcano_2_upper_descent',
	'volcano_2_upper_secret',
	'volcano_3_core',
	'volcano_3_top',
	'volcano_3_middle',
	'volcano_3_bottom',
	'volcano_3_secret'
]

STARS_BG = [
	'rope_test',
	'ship_1'
]





##########################################

_bg = {}
for cbg in CAVE_BG:
	_bg[cbg] = 'cave'
for vbg in VOLCANO_BG:
	_bg[vbg] = 'volcano'
for sbg in STARS_BG:
	_bg[sbg] = 'stars'


def getBackground(level):
	level = level.split('.')[0]
	return _bg.get(level, 'sky')
