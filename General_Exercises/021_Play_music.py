import pygame
def blue_danube():
    '''This funcition plays one of the most beautiful songs ever created - The Blue Danube Waltz'''
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load('021_the_blue_danube_waltz.mp3')
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    input()
    pygame.event.wait()

blue_danube()

