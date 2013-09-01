_imageLibrary = {}

def getImage(path):
	img = _imageLibrary.get(path)
	if img == None:
		alphaImg = pygame.image.load(('images/' + path).replace('/', os.sep).replace('\\', os.sep))
		magenta = pygame.Surface(alphaImg.get_size()).convert()
		magenta.fill((255, 0, 255))
		magenta.blit(alphaImg, (0, 0))
		magenta.set_colorkey((255, 0, 255))
		img = magenta
		_imageLibrary[path] = img
	return img