import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
speed = 5
running = True
rect1x = 20
rect1y = 20
rect1w = 20
rect1h = 20
RED = (255, 0, 0)
GREEN = (0, 255,0)
GREY = (90, 90, 90)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

rect = pygame.Rect(rect1x, rect1y, rect1w, rect1h)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        rect.x = rect1x +10
        rect.y = rect1y + 10
    if keys[pygame.K_1]:
        rect.x += 1
        rect.y += 1
    
    screen.fill(GREEN)
    pygame.draw.rect(screen, (0, 0, 0), rect)
    pygame.display.update()

pygame.quit()
