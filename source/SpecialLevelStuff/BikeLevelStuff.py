class BikeLevelStuff(SpecialLevelStuff):
	def __init__(self, scene):
		SpecialLevelStuff.__init__(self, scene)
		self.hasUpdate = True
		self.hasRender = True
		
	def update(self):
		
		scene = self.scene
		player = scene.player
		if player.x > (scene.cols - 1) * 16: # one less because you can't technically go off screen
			scene.next = VictorySequenceScene(scene)
	
	def render(self, screen, rc, offsetX, offsetY):
		p = self.scene.player
		px = p.x + offsetX
		py = p.y + offsetY
		i = 0
		while i < 30:
			y = py + i * 12 + (rc % 12)
			x = px + int(math.sin(rc * 2 * 3.14159 / 60) * 24 * i) * (-1 if (i % 2 == 0) else 1)
			PDR(screen, (255, 255, 128), pygame.Rect(x, y, 4, 4))
			i += 1
		
		
		screen.blit(getText(WHITE, "Don't worry, I'll redo the"), (0, 8))
		screen.blit(getText(WHITE, "scatter pattern before"), (0, 16))
		screen.blit(getText(WHITE, "we turn it in."), (0, 24))
		screen.blit(getText(WHITE, "              --Blake"), (0, 32))