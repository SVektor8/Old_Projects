from tkinter import *
from pygame import *
from math import *
from Feugenbaum_Helper42 import *

def qeq(mas,i):
    global sc
    for j in mas:
        draw.circle(sc, WHITE, (i, int(700*(1-j))), 1)

def do():
    sc.fill(BERLIN_LAZUR)
    for i in range(1,10):
        draw.line(sc, Kinovar, (0, i/10*700), (1200, i/10*700))
    for i in range(1,12):
        draw.line(sc,Kinovar, (i*100,0), (i*100,700))

print()
print('Feugenbaum_Diagram 4.2')
print('By Vektor')
print()

FPS = 100
W = 1200  # ширина экрана
H = 700  # высота экрана
DARKKHAKI = (189, 183, 107)
OLIVE = (128, 128, 0)
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
RED = (225, 0, 50)
GREEN = (0, 225, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BERLIN_LAZUR = (0, 49, 83)
Luminescent_Red = (248, 0, 0)
Alii = (255, 36, 0)
Kinovar = (255, 77, 0)
Yellow_lazer_limon = (254,254,34)


print('Стрелочки -- движение влево-вправо, вверх-вниз')
print('A/D -- уменьшение/увеличение масштаба по горизонтали')
print('S/W -- уменьшение/увеличение масштаба по вертикали')
print('Пробел -- сгенерировать диаграмму')
print()
print('Input maximal zoom and press Enter')


Nmax = int(input())

graph = graph_creator(W, Nmax)

init()
clock = time.Clock()
sc = display.set_mode((W,H))

delta = 1
Nx = Nmax
Ny = Nmax
movex = 0
movey = 0
dy = 0
dx = 0
Centerx = W//2 * Nx
Centery = 0.5
updating = False

print()

    
while 1:

    if (abs(movex)+abs(movey)+abs(dx)+abs(dy)!=0) or updating:

        updating = False
        
        sc.fill(BERLIN_LAZUR)
        for i in range(1,10):
            draw.line(sc, Kinovar, (0, i/10*700), (1200, i/10*700))
        for i in range(1,17):
            draw.line(sc,Kinovar, (i*70,0), (i*70,700))

        if (Nx-dx>=1): #and (Nx-dx<=Nmax):
            Nx-=dx
            dx = 0
        if (Ny+dy>=1): #and (Ny-dy<=Nmax):
            Ny+=dy
            dy = 0

        Centerx += (Nx*movex)
        Centery -= movey/(Ny-Nmax+1)
        

        
        q = 0
        for i in range(Centerx - W//2 * Nx,Centerx + W//2 * Nx,Nx):
            if i>=0 and i <len(graph):
                for j in graph[i]:
                    yyy = int( (Centery - j) * H *(Ny-Nmax+1) + H//2 )
                    if yyy<H and yyy>0: 
                        draw.line(sc, WHITE, (q, yyy), (q, yyy))
            q+=1

        #print(Nx, Ny)
        

        display.update()
    
    for i in event.get():
        if i.type == QUIT:
            exit()
        elif i.type == KEYDOWN:
            if i.key == K_LEFT:
                movex = -delta*10
            if i.key == K_RIGHT:
                movex = delta*10
            if i.key == K_UP:
                movey = -delta*0.02
            if i.key == K_DOWN:
                movey = delta*0.02
            if i.key == K_w:
                dy = delta
            if i.key == K_s:
                dy = -delta
            if i.key == K_a:
                dx = -delta
            if i.key == K_d:
                dx = delta
            if i.key == K_BACKSPACE:
                print()
                print('Input maximal zoom and press Enter')
                Nmax = int(input())
                print()
                graph = graph_creator(W, Nmax)
            
            if i.key == K_SPACE:
               updating = True
                        
        elif i.type == KEYUP:
            if i.key in [K_LEFT, K_RIGHT]:
                movex = 0
            if i.key in [K_UP, K_DOWN]:
                movey  = 0
            if i.key in [K_w, K_s]:
                dy  = 0
            if i.key in [K_d, K_d]:
                dx  = 0
                                
            #elif i.key == pygame.K_UP:
            #elif i.key == pygame.K_DOWN:
        #elif i.type == pygame.MOUSEBUTTONDOWN:
            #if i.button == 1:
                
    
    clock.tick(FPS)
