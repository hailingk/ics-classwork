import pygame
import random as rd
from pygame.locals import QUIT

pygame.init()

width = 800
height = 800
size = (width, height)
cloud_x = 70
cloud_y = 100
sun_x=-40
sun_y=500
cloud_x1 = 500
cloud_y1 = 100

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True
while running:
  for event in pygame.event.get():
        if event.type == QUIT:
            running = False

  #sky
  screen.fill((204, 255, 255))  

  #grass
  pygame.draw.rect(screen, (7, 136, 70), (0,700 ,1000 ,100))
  #house
  pygame.draw.rect(screen, (185,156,107), (250, 400,300,300))
  #chimney
  pygame.draw.rect(screen,(185,156,107),(475,300, 50, 100 ))
#sun
  pygame.draw.circle(screen,(250,253,15),(sun_x,sun_y),40)

  if sun_x >=400 or sun_y <= 100:
    sun_x += 3
    sun_y +=3
  if sun_x < 400 :
    sun_x +=5
    sun_y -=5
  if sun_x > 800:
    sun_x = -40
    
#cloud
  if cloud_x > 1000:
    cloud_x = -100
  else:
    cloud_x += 4

  if cloud_x1 > 1000:
    cloud_x1 = -100
  else:
    cloud_x1 += 4

  pygame.draw.circle(screen,(255,255,255),(cloud_x,cloud_y),55)
  pygame.draw.circle(screen,(255,255,255),(cloud_x+61,cloud_y-5),45) 
  pygame.draw.circle(screen,(255,255,255),(cloud_x+10,cloud_y+36),40)
  pygame.draw.circle(screen,(255,255,255),(cloud_x-51,cloud_y+23),40)
  pygame.draw.circle(screen,(255,255,255),(cloud_x+71,cloud_y+32),40)

  pygame.draw.circle(screen,(255,255,255),(cloud_x1,cloud_y1),55)
  pygame.draw.circle(screen,(255,255,255),(cloud_x1+61,cloud_y1-5),45) 
  pygame.draw.circle(screen,(255,255,255),(cloud_x1+10,cloud_y1+36),40)
  pygame.draw.circle(screen,(255,255,255),(cloud_x1-51,cloud_y1+23),40)
  pygame.draw.circle(screen,(255,255,255),(cloud_x1+71,cloud_y1+32),40)
  #smoke 
  for i in range(0,20):
      x = rd.randint(475, 525)
      y = rd.randint(10, 290)
      radius = rd.randint(1,7)
      color = rd.randint(50,200)
      pygame.draw.circle(screen,(color,color,color), (x,y), radius  )
      

  #roof
  pygame.draw.polygon(screen, (119,21,21),((250,400),(400,300),(550,400) ) )

  #door
  pygame.draw.rect(screen,(119,21,21),(375,600,50,100 ))
  #handle
  pygame.draw.circle(screen, (253,156,15), (415,650), 5)
  #windows
  pygame.draw.rect(screen, (0,96,255), (300,450,50, 50))
  pygame.draw.rect(screen, (0,96,255), (450,450,50, 50))
  pygame.draw.rect(screen, (0,96,255), (300,550,50, 50))
  pygame.draw.rect(screen, (0,96,255), (450,550,50, 50))
  #tree trunks
  pygame.draw.rect(screen,(100,100,100), (100,500, 50, 200))
  pygame.draw.rect(screen,(100,100,100), (650,500, 50, 200))
  #tree leaf
  pygame.draw.polygon(screen, (0,200,50),((25,650),(125,550),(225,650) ) )
  pygame.draw.polygon(screen, (0,200,50),((35,600),(125,510),(215,600) ) )
  pygame.draw.polygon(screen, (0,200,50),((45,550),(125,470),(205,550) ) )
  
  pygame.draw.polygon(screen, (0,200,50),((575,650),(675,550),(775,650) ) )
  pygame.draw.polygon(screen, (0,200,50),((585,600),(675,510),(765,600) ) )
  pygame.draw.polygon(screen, (0,200,50),((595,550),(675,470),(755,550) ) )






    
  
  pygame.display.flip()
  clock.tick(30)
  

pygame.quit()
    
