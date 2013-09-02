def SPRITE_renderPlayerOver(sprite, screen, offsetX, offsetY, rc):
	pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(sprite.x + offsetX - 8, sprite.y + offsetY - 8, 16, 16))

class Sprite:
	def __init__(self, type, px, py):
		self.type = type
		self.x = px
		self.y = py
		self.modelX = px + 0.0
		self.modelY = py + 0.0
		
		
		self.renderImpl = SPRITE_renderPlayerOver
		
	def update(self, scene):
		if self.dx != 0 or self.dy != 0:
			newx = self.modelX + self.dx
			newy = self.modelY + self.dy
			col = int(newx / 16)
			row = int(newy / 16)
			if scene.passable[col][row]:
				self.modelX = newx
				self.modelY = newy
				self.x = int(self.modelX)
				self.y = int(self.modelY)
			self.dx = 0
			self.dy = 0
	
	def render(self, screen, offsetX, offsetY, rc):
		self.renderImpl(self, screen, offsetX, offsetY, rc)