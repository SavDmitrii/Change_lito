import pygame
import sys
from stations import Station
from random import randint as r


pygame.init()

screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption('Colors')

def random_x():
    return r(400, 410)
def random_y():
    return r(350, 365)


bg = pygame.image.load('images/bg_color.jpg')
station_1 = Station(random_x(), random_y(), 'images/color_1.png')
station_2 = Station(random_x(), random_y(), 'images/color_2.png')
station_3 = Station(random_x(), random_y(), 'images/color_3.png')

stantions = [station_1, station_2, station_3]

a = 1

def change_station(num):
    return stantions[num]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                stantion.rect.x += 2

            elif event.key == pygame.K_LEFT:
                stantion.rect.x -= 2
                
            elif event.key == pygame.K_UP:
                stantion.rect.y -= 2

            elif event.key == pygame.K_DOWN:
                stantion.rect.y += 2
                
            elif event.key == pygame.K_1:
                a = 0
            elif event.key == pygame.K_2:
                a = 1
            elif event.key == pygame.K_3:
                a = 2
                
    stantion = change_station(a)
    screen.fill((0, 0, 0))
    screen.blit(bg, (20, 30))
    for i in stantions:
        screen.blit(i.image, i.rect)
        
    # screen.blit(station_1.image, station_1.rect)
    # screen.blit(station_2.image, station_2.rect)
    # screen.blit(station_3.image, station_3.rect)
    pygame.display.update()

            