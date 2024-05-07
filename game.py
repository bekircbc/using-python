import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

runnig = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((0,0,0))

  pygame.draw.circle(screen, (255,0,0), (400,300), 50)

  pygame.display.flip()

pygame.quit()
