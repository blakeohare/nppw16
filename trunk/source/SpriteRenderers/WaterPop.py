
def SPRITE_renderWaterPop(sprite, scene, screen, offsetX, offsetY, arc):
	
	left = sprite.x + offsetX - 24
	top = sprite.y + offsetY - 8
	print("WORKS", left, top, sprite.x, sprite.y)
	screen.blit(getImage('tiles/balloons/pop.png'), (left, top))
