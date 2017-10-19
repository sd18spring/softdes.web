import os
import pygame

pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"

width, height = 640, 480

screen = pygame.display.set_mode((width, height))


class Ball:
    def __init__(self, x, y, dy=1):
        self.x = x
        self.y = y
        self.dy = dy

    def draw(self):
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 50)

    def step(self):
        self.y += self.dy
        self.dy += 1
        self.dy *= 0.99
        if self.y > height:
            self.dy = -self.dy


ball = Ball(width / 2, height / 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            ball.y = 0
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    ball.draw()
    ball.step()
    pygame.display.update()

pygame.quit()
