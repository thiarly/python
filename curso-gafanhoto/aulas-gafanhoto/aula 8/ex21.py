#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('/Users/thiarly/Desktop/python/curso-gafanhoto/ex-gafanhoto/charli0100.mp3')
pygame.mixer.music.play()
input()
#pygame.event.wait()


##########################################################################################################
#import pygame as pygame

#pygame.mixer.init()
#pygame.mixer.music.load('/Users/thiarly/Desktop/python/curso-gafanhoto/ex-gafanhoto/program.mp3')
#def play():
#   timer = 1
#    pygame.mixer.music.play()
#    timer = 2
#   if timer == 2:
#        play()

#play()
###########################################################################################################
