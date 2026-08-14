# import winsound
#
# winsound.Beep(500, 1000)

import pygame
pygame.init()
pygame.mixer.music.load("ex019.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()