
def SPRITE_renderSeed(sprite, scene, screen, offsetX, offsetY, arc):
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	img = getImage('sprites/bird_seed.png')
	screen.blit(img, (left, top))
