
def SPRITE_renderGravityDevice(sprite, scene, screen, offsetX, offsetY, arc):
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	
	screen.blit(getImage('sprites/gravity_device.png'), (left, top))
