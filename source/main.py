FPS = 30
WIDTH = int(256 * 3.4)
HEIGHT = 224 * 3

def main():
	pygame.init()
	
	real_screen = pygame.display.set_mode((WIDTH, HEIGHT))
	virtual_screen = pygame.Surface((256, 224))
	
	activeScene = OpeningScene()
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
				
			if event.type == pygame.KEYDOWN and event.key == pygame.K_F4 and altPressed:
				quitAttempt = True
			
			if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
				down = event.type == pygame.KEYDOWN
				if event.key == pygame.K_RETURN:
					events.append(MyEvent('start', down))
				elif event.key == pygame.K_LEFT:
					events.append(MyEvent('left', down))
				elif event.key == pygame.K_RIGHT:
					events.append(MyEvent('right', down))
				elif event.key == pygame.K_UP:
					events.append(MyEvent('up', down))
				elif event.key == pygame.K_DOWN:
					events.append(MyEvent('down', down))
					
		if quitAttempt:
			activeScene = None
			
		if activeScene != None:
			largeScreen = 'W' in activeScene.flags
			
			activeScene.processInput(events, {})
			activeScene.update()
			if largeScreen:
				activeScene.render(real_screen, renderCounter)
			else:
				activeScene.render(virtual_screen, renderCounter)
			
			activeScene = activeScene.next
			
			if not largeScreen:
				pygame.transform.scale(virtual_screen, (WIDTH, HEIGHT), real_screen)
			
			pygame.display.flip()
		
		renderCounter += 1
		
		end = time.time()
		
		diff = end - begin
		
		delay = 1.0 / FPS - diff
		if delay > 0:
			time.sleep(delay)


main()