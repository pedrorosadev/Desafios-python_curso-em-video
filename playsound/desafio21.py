import pygame

#Incializando o Pygame
pygame.init()
pygame.mixer.init()

#Carregando e dando o Play na Música.
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
input() #Mantém o programa aberto.
