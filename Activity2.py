import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("pygame window")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Circle positions and radius
outline_pos = (100, 100)
filled_pos = (300, 250)
radius = 40
thickness = 3  # For the outline circle

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
# fill background
screen.fill(WHITE)

# draw outline circle
pygame.draw.circle(screen, GREEN, outline_pos, radius, thickness)

#draw filled circle
pygame.draw.circle(screen, GREEN, filled_pos, radius)

# update the display
pygame.display.flip()

# quit
pygame.quit()
sys.exit()
