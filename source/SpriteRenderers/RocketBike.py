
def SPRITE_renderRocketBike(sprite, scene, screen, offsetX, offsetY, arc):
	left = sprite.x + offsetX - 16
	top = sprite.y + offsetY - 24
	img = getImage('sprites/rocket_bike_squirrelless.png')
	screen.blit(img, (left, top))
