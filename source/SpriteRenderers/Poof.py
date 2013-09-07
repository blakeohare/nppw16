
def SPRITE_renderPoof(sprite, scene, screen, offsetX, offsetY, arc):
	isBig = sprite.automation.isBig
	left = sprite.x + offsetX - 8
	top = sprite.y + offsetY - 8
	
	c = sprite.automation.counter
	if c <= 3:
		num = '1'
	elif c <= 6:
		num = '2'
	elif c <= 9:
		num = '3'
	else:
		return
	
	if isBig:
		top -= 16
		img = getImage('sprites/large_poof_' + num + '.png')
	else:
		img = getImage('sprites/small_poof_' + num + '.png')
	
	screen.blit(img, (left, top))
