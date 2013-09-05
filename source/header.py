import math
import os
import random
import pygame
import time

DEBUG = True
SOUND_ENABLED = False

if not DEBUG:
	SOUND_ENABLED = True

GO_TO_TITLE = DEBUG
SHOW_FRAME_DROP = DEBUG