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

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
x, y = 925, 75


f = pygame.font.SysFont('arialunicode', 24)
sc_text1 = f.render('Станция 1', 1, WHITE)
sc_text2 = f.render('Станция 2', 1, WHITE)
sc_text3 = f.render('Станция 3', 1, WHITE)
pos1 = sc_text1.get_rect(center=(1000, 100))
pos2 = sc_text2.get_rect(center=(1000, 150))
pos3 = sc_text3.get_rect(center=(1000, 200))


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
                y = 75
            elif event.key == pygame.K_2:
                a = 1
                y = 125
            elif event.key == pygame.K_3:
                a = 2
                y = 175
                
    stantion = change_station(a)
    screen.fill((0, 0, 0))
    screen.blit(bg, (20, 30))
    for i in stantions:
        screen.blit(i.image, i.rect)
        
    # screen.blit(station_1.image, station_1.rect)
    # screen.blit(station_2.image, station_2.rect)
    # screen.blit(station_3.image, station_3.rect)
    pygame.draw.rect(screen, GREEN, (x, y, 150, 50), 2)
    
    screen.blit(sc_text1, pos1)
    screen.blit(sc_text2, pos2)
    screen.blit(sc_text3, pos3)

    pygame.display.update()

            