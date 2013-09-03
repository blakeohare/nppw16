_imageLibrary = {}
_reversedLibrary = {}

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

def getBackwardsImage(path):
	img = _reversedLibrary.get(path)
	if img == None:
		img = getImage(path)
		img = pygame.transform.flip(img, True, False)
		_reversedLibrary[path] = img
	return img