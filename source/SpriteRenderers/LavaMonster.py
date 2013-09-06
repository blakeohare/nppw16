def SPRITE_renderLavaMonster(sprite, scene, screen, offsetX, offsetY, arc):

	left = sprite.x - 8 + offsetX
	top = sprite.y - 24 + offsetY
	
	
	if sprite.automation.mouthOpen:
		path = 'sprites/lava_monster_2.png'
	else:
		path = 'sprites/lava_monster_1.png'
	if sprite.lastDirection == 'left':
		img = getBackwardsImage(path)
	else:
		img = getImage(path)
	
	screen.blit(img, (left, top))