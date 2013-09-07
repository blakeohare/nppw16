def SPRITE_renderMoonSquid(sprite, scene, screen, offsetX, offsetY, arc):
	left = offsetX + sprite.x - 8
	top = offsetY + sprite.y - 8
	
	img = getImage('sprites/moonsquid_1.png' if ((arc & 1) == 0) else 'sprites/moonsquid_2.png')
	screen.blit(img, (left, top))
	