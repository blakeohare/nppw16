
def SPRITE_renderAcornTop(sprite, scene, screen, offsetX, offsetY, arc):
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	width = 16
	height = 16
	path = 'acorn_projectile_1'
	path = 'sprites/' + path + '.png'
	img = getImage(path)
	screen.blit(img, (left, top))
