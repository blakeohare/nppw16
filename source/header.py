import math
import os
import random
import pygame
import time

DEBUG_MODE = True
SOUND_ENABLED = True

if not DEBUG_MODE:
	SOUND_ENABLED = True

GO_TO_TITLE = DEBUG_MODE
SHOW_FRAME_DROP = DEBUG_MODE