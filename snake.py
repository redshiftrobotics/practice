# Open terminal, make sure conda env is correct `pip install pygame`
import pygame

# Game settings
game_over = False
grid_width = 400
grid_height = 300
grid_size = 10

# Pygame init
pygame.init()
dis = pygame.display.set_mode((grid_width, grid_height))
pygame.display.set_caption('Snake game')

class Snake():
    def __init__(self):
        self.x = grid_width / 2
        self.y = grid_height / 2

        self.dx = grid_size
        self.dy = 0
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
        pygame.draw.rect(dis, (0, 0, 255), [self.x, self.y, grid_size, grid_size])

    def move(self, dx, dy):
        self.dx = dx
        self.dy = dy

snake = Snake()
clock = pygame.time.Clock()

# Game loop
while not game_over:
    dis.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    
    snake.update()
    pygame.display.update()
    clock.tick(5)

pygame.quit()
quit()