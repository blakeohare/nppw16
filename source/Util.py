WHITESPACE = ' \r\n\t'
def trim(string):
	while len(string) > 0 and string[0] in WHITESPACE:
		string = string[1:]
	while len(string) > 0 and string[-1] in WHITESPACE:
		string = string[:-1]
	return string

def makeGrid(width, height):
	cols = []
	while width > 0:
		cols.append([None] * height)
		width -= 1
	return cols

class StemCell:
	def __init__(self):
		pass
	

def drawBox(screen, x, y, cols, rows):
	left = x
	top = y
	bottom = y + (rows - 1) * 8
	right = x + (cols - 1) * 8
	screen.blit(getImage('misc/border_nw.png'), (left, top))
	screen.blit(getImage('misc/border_ne.png'), (right, top))
	screen.blit(getImage('misc/border_se.png'), (right, bottom))
	screen.blit(getImage('misc/border_sw.png'), (left, bottom))
	x = left + 8
	while x < right:
		screen.blit(getImage('misc/border_n.png'), (x, top))
		screen.blit(getImage('misc/border_s.png'), (x, bottom))
		x += 8
	y = top + 8
	while y < bottom:
		screen.blit(getImage('misc/border_w.png'), (left, y))
		screen.blit(getImage('misc/border_e.png'), (right, y))
		y += 8
	
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(left + 8, top + 8, right - left - 8, bottom - top - 8))
	
def legacyMap(fun, things):
	output = []
	for thing in things:
		output.append(fun(thing))
	return output