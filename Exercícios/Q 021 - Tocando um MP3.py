import pygame
pygame.mixer.init()
pygame.init()

pygame.mixer.music.load('disco.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
