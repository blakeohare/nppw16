PDR = pygame.draw.rect
YELLOW = (255, 255, 0)
def SPRITE_renderLazor(sprite, scene, screen, offsetX, offsetY, arc):
	x = offsetX + sprite.x - 8
	y = offsetY + sprite.y - 2
	PDR(screen, YELLOW, pygame.Rect(x, y, 16, 4))