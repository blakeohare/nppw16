class BikeLevelStuff(SpecialLevelStuff):
	def __init__(self, scene):
		SpecialLevelStuff.__init__(self, scene)
		self.hasUpdate = True
		self.hasRender = True
		self.particles = []
		self.counter = 0
		
	def update(self):
		if self.counter == 0:
			self.scene.sprites.append(Sprite('bird2', 16, 48))
		self.counter += 1
		scene = self.scene
		player = scene.player
		if player.x > (scene.cols - 1) * 16: # one less because you can't technically go off screen
			scene.next = VictorySequenceScene(scene)
		
		if self.counter % 2 == 0:
			pt = StemCell()
			pt.x = player.x
			pt.y = player.y
			pt.vx = random.random() * 16 - 8
			pt.vy = random.random() * 6 - 5
			self.particles.append(pt)
		
		for pt in self.particles:
			pt.x += pt.vx
			pt.y += pt.vy
			pt.vy += 2
	
	def render(self, screen, rc, offsetX, offsetY):
		p = self.scene.player
		px = p.x + offsetX
		py = p.y + offsetY
		
		for pt in self.particles:
			PDR(screen, (255, 255, 128), pygame.Rect(pt.x + offsetX, pt.y + offsetY, 3, 3))
		
		if len(self.particles) > 40:
			self.particles = self.particles[1:]
		
		
		#screen.blit(getText(WHITE, "Don't worry, I'll redo the"), (0, 8))
		#screen.blit(getText(WHITE, "scatter pattern before"), (0, 16))
		#screen.blit(getText(WHITE, "we turn it in."), (0, 24))
		#screen.blit(getText(WHITE, "              --Blake"), (0, 32))