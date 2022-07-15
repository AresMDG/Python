#1
from operator import le, length_hint
import pygame
from random import randrange

RES = 1000
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirst = {'W': True, 'S': True, 'A': True, 'D': True,}
length = 1
snake = [(x,y)]
dx, dy = 0, 0
score = 0
fps = 5 

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score =  pygame.font.SysFont('Arial', 26, bold = True)
font_end = pygame.font.SysFont('Arial', 66, bold = True)

while True:
   sc.fill(pygame.Color('black'))
   
   #* Drawing snake
   [(pygame.draw.rect(sc, pygame.Color('green'),(i, j, SIZE, SIZE))) for i, j in snake] 
   
   #* Drawing apple
   pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))
   
   #* Show score
   render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('orange'))
   sc.blit(render_score, (5, 5))
   
   #* Move snake
   x += dx * SIZE
   y += dy * SIZE
   snake.append((x, y))
   snake = snake [-length:]
   
   
   #* Eating
   if snake[-1] == apple:
      apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
      length += 1
      score += 1
      fps += 1   
      
   #* Game over
   if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
      while True:
         render_end = font_end.render('GAME OVER', 1, pygame.Color('red'))
         sc.blit(render_end, (RES // 2 - 200, RES // 3 ))
         pygame.dislpay.flip()
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit()
         
   
   pygame.display.flip()
   clock.tick(fps)
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         exit()
   
   #* Control Snake
   key = pygame.key.get_pressed()
   if key [pygame.K_w] and dirst['W']:
      dx, dy = 0, -1
      dirst = {'W': True, 'S': True, 'A': True, 'D': True,}
   if key [pygame.K_s] and dirst['S']:
      dx, dy = 0, 1
      dirst = {'W': True, 'S': True, 'A': True, 'D': True,}
   if key [pygame.K_a] and dirst['A']:
      dx, dy = -1, 0
      dirst = {'W': True, 'S': True, 'A': True, 'D': True,}
   if key [pygame.K_d] and dirst['D']:
      dx, dy = 1, 0
      dirst = {'W': True, 'S': True, 'A': True, 'D': True,}