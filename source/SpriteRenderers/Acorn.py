
def SPRITE_renderAcorn(sprite, scene, screen, offsetX, offsetY, arc):
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	width = 16
	height = 16
	
	if sprite.moving:
		path = 'acorn_' + '13'[(arc // 2) & 1]
	else:
		path = 'acorn_2'
	
	path = 'sprites/' + path + '.png'
	reverse = sprite.lastDirection == 'left'
	if reverse:
		img = getBackwardsImage(path)
	else:
		img = getImage(path)
	screen.blit(img, (left, top))
