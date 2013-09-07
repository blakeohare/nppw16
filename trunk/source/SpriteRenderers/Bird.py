
def SPRITE_renderBird(sprite, scene, screen, offsetX, offsetY, arc):
	left = sprite.x + offsetX - 16
	top = sprite.y + offsetY - 16
	img = getImage('sprites/bird_chase_' + ('1' if (((arc // 2) & 1) == 0) else '2') + '.png')
	screen.blit(img, (left, top))
