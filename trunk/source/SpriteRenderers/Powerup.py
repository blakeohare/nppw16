
def SPRITE_renderPowerup(sprite, scene, screen, offsetX, offsetY, arc):
	
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	type = sprite.powerupInfo.type
	if type == '1up':
		path = 'sprites/1up.png'
	elif type == 'life_small':
		path = 'sprites/life_small.png'
	elif type == 'life_big':
		path = 'sprites/life_big.png'
	
	screen.blit(getImage(path), (left, top))
