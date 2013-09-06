
def SPRITE_renderAcorn(sprite, scene, screen, offsetX, offsetY, arc):
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	width = 16
	height = 16

	base = 'acorn'
	if sprite.automation.mode in ('throwing', 'baldpatrolling'):
		base = 'acorn_capless'
	
	if sprite.moving:
		path = base + '_' + '13'[(arc // 2) & 1]
	else:
		path = base + '_2'
	
	path = 'sprites/' + path + '.png'
	reverse = sprite.lastDirection == 'left'
	if reverse:
		img = getBackwardsImage(path)
	else:
		img = getImage(path)
	screen.blit(img, (left, top))
