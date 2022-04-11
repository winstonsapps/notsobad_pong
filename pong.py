# made with pygame 2.1.2


import pygame, sys
from math import sin,cos,pi

pygame.init()

size = width,height = 1280, 720

black = (0, 0, 0) # black

white = (255,255,255) # white

screen = pygame.display.set_mode(size)

pygame.display.set_caption('poing!')

clock = pygame.time.Clock()
def draw(side, offset, circlecoords=(0,0)): #side: string = 'left' or 'right'or 'circle', height = int, returns a rect
    if side == 'left':
        pygame.draw.line(screen, white, (30, 50+offset), (30 , -50+offset), 16)
        return(pygame.draw.line(screen, white, (30, 50+offset), (30 , -50+offset), 16))
    if side == 'right':
        pygame.draw.line(screen, white, (1250, 50+offset), (1250 , -50+offset), 16)
        return(pygame.draw.line(screen, white, (1250, 50+offset), (1250 , -50+offset), 16))
    if side == 'circle':
        pygame.draw.circle(screen, white, circlecoords, speed)
        return(pygame.draw.circle(screen, white, circlecoords, speed*4+7))

def move_dir(steps, direction): #changes number and direction to x,y shifts
    
    return((steps * sin((direction * pi/180)), steps * cos((direction * pi/180))))
    
    
lefty = 0
righty = 0
circlex = 640
speed = 6
circley = 300
circle_dir = 90
circlerect = None
leftrect = None
rightrect = None
temp = 0,0
p1points = 0
p2points = 0
max_speed = 14
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        lefty -= speed
        if lefty > 720 or lefty < 0:
            lefty += speed
    if keys[pygame.K_s]:
        lefty += speed
        if lefty > 720 or lefty < 0:
            lefty -= speed
    if keys[pygame.K_UP]:
        righty -= speed
        if righty > 720 or righty < 0:
            righty += speed
    if keys[pygame.K_DOWN]:
        righty += speed
        if righty > 720 or righty < 0:
            righty -= speed 
    
    temp = move_dir(speed, circle_dir)
    circlex += temp[0]
    circley -= temp[1]
    if circley > 720:
        circle_dir = 180 - circle_dir
        circle_dir = 360 + circle_dir
        if not speed == max_speed:
            speed+=0.2
    if circley < 0:
        circle_dir = 180 - circle_dir
        circle_dir = 360 + circle_dir
        if not speed == max_speed:
            speed+=0.2
        
    screen.fill(black)
    

    leftrect = draw('left', lefty)
    rightrect = draw('right', righty)
    circlerect = draw('circle', 0, [circlex, circley])
    
    if circlerect.colliderect(leftrect):
        if not speed == max_speed:
            speed+=0.2
        off = circley - lefty
        circle_dir = 270 - circle_dir
        circle_dir = 270 + circle_dir - 180 - off
    if circlerect.colliderect(rightrect):
        if not speed == max_speed:
            speed+=0.2
        off = circley - righty
        
        circle_dir = 90 - circle_dir
        circle_dir = 90 + circle_dir + 180 - off
        
    if(circlex > 1280):
        p1points +=1
        print('player 1 points: ', (p1points))
        circlex = 640
        circley = 480
        
    if(circlex<0):
        p2points +=1
        print('player 2 points: ', (p2points))
        circlex = 640
        circley = 480
    if p1points == 10:
        print('player 1 wins')
        sys.exit()
    if p2points == 10:
        print('player 2 wins')
        sys.exit()
    
        
        
    
    
            
           
    pygame.display.flip()

    clock.tick(60)
    
    
pygame.quit()
 
            