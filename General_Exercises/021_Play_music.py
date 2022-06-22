import pygame
def blue_danube():
    '''This funcition plays one of the most beautiful songs ever created - The Blue Danube Waltz'''
    pygame.init()                                           #Iniciando a biblioteca
    pygame.mixer.music.load('The_Blue_Danube_Waltz.mp3')    #Escolha da música
    #pygame.mixer.music.play()                               #Tocar a música
    #pygame.event.wait()                                     #Esperar a música acabar

blue_danube()
