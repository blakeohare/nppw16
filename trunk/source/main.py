FPS = 30
WIDTH = 800
HEIGHT = 600

def main():
	pygame.init()
	
	real_screen = pygame.display.set_mode((WIDTH, HEIGHT))
	virtual_screen = pygame.Surface((256, 224))
	
	activeScene = TitleScene()
	renderCounter = 0
	while activeScene != None:
		begin = time.time()
		events = []
		quitAttempt = False
		pressedKeys = pygame.key.get_pressed()
		altPressed = pressedKeys[pygame.K_LALT] or pressedKeys[pygame.K_RALT]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quitAttempt = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_F4 and altPressed:
					quitAttempt = True
		
		
		if quitAttempt:
			activeScene = None
			
		if activeScene != None:
			activeScene.processInput(events, {})
			activeScene.update()
			activeScene.render(virtual_screen, renderCounter)
			
			activeScene = activeScene.next
			
			pygame.transform.scale(virtual_screen, (WIDTH, HEIGHT), real_screen)
			
			pygame.display.flip()
		
		end = time.time()
		
		diff = end - begin
		
		delay = 1.0 / FPS - diff
		if delay > 0:
			time.sleep(delay)


main()