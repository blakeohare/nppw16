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