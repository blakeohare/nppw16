
def SPRITE_renderByat(sprite, scene, screen, offsetX, offsetY, arc):
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	if sprite.automation.perched:
		path = 'sprites/byat_hang.png'
	else:
		if (arc & 1) == 0:
			path = 'sprites/byat_fly_1.png'
		else:
			path = 'sprites/byat_fly_2.png'
	
	if sprite.lastDirection == 'left':
		img = getBackwardsImage(path)
	else:
		img = getImage(path)
		
	screen.blit(img, (left, top))
