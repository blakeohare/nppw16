NEIGHBOR_RANGE = (-1, 0, 1)

def SPRITE_renderPlayerOver(sprite, screen, offsetX, offsetY, rc):
	pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(sprite.x + offsetX - 8, sprite.y + offsetY - 8, 16, 16))

XY_PAIRINGS = [
	(0, 0),
	(1, 0),
	(2, 0),
	(3, 0),
	(4, 0),
	(4, 1),
	(4, 2),
	(4, 3)
]

class Sprite:
	def __init__(self, type, px, py):
		self.type = type
		self.x = px
		self.y = py
		self.modelX = px + 0.0
		self.modelY = py + 0.0
		self.xs = [None] * 5
		self.ys = [None] * 5
		
		self.neighbors = [None] * 36
		self.renderImpl = SPRITE_renderPlayerOver
		
	def checkNeighborCollision(self, scene, col, row, targetX, targetY):
		area_left = targetX - 5
		area_right = targetX + 5
		area_top = targetY - 5
		area_bottom = targetY + 5
		
		width = scene.cols
		height = scene.rows
		left = col - 2
		right = col + 2
		top = row - 2
		bottom = row + 2
		if left < 0: left = 0
		if right >= width: right = width - 1
		if top < 0: top = 0
		if bottom >= height: bottom = height - 1
		index = 0
		y = top
		while y <= bottom:
			x = left
			while x <= right:
				cs = scene.tiles[x][y].collisions
				csi = len(cs) - 1
				while csi >= 0:
					self.neighbors[index] = cs[csi]
					csi -= 1
					index += 1
				x += 1
			y += 1
		
		index -= 1
		while index >= 0:
			n = self.neighbors[index]
			if n[0] > area_right:
				pass
			elif n[1] > area_bottom:
				pass
			elif n[2] < area_left:
				pass
			elif n[3] < area_top:
				pass
			else:
				return False
			index -= 1
		return True
		
	def update(self, scene):
		if scene.side:
			pass
		else:
			if self.dx != 0 or self.dy != 0:
				xs = self.xs
				ys = self.ys
				
				xs[0] = self.modelX + self.dx
				xs[1] = self.modelX + self.dx * 3.0 / 4
				xs[2] = self.modelX + self.dx / 2.0
				xs[3] = self.modelX + self.dx / 4.0
				xs[4] = self.modelX
				
				ys[0] = self.modelY + self.dy
				ys[1] = self.modelY + self.dy * 3.0 / 4
				ys[2] = self.modelY + self.dy / 2.0
				ys[3] = self.modelY + self.dy / 4.0

				for pairing in XY_PAIRINGS:
					newx = xs[pairing[0]]
					newy = ys[pairing[1]]
					col = int(newx / 16)
					row = int(newy / 16)

					if self.checkNeighborCollision(scene, col, row, newx, newy):
						self.modelX = newx
						self.modelY = newy
						self.x = int(self.modelX)
						self.y = int(self.modelY)
						break
				
				self.dx = 0
				self.dy = 0
	
	def render(self, screen, offsetX, offsetY, rc):
		self.renderImpl(self, screen, offsetX, offsetY, rc)