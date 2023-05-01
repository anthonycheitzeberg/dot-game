import pygame
from src.maps.map import TileMap
from src.shared import constants


class Game:
    def __init__(self):
        self.running = True
        self.screen_size = (constants.SCREEN_DIMENSIONS['WIDTH'], constants.SCREEN_DIMENSIONS['HEIGHT'])

    def main_loop(self):
        # Initialize Pygame
        pygame.init()
        screen = pygame.display.set_mode(self.screen_size)
        clock = pygame.time.Clock()
        tile_map = TileMap('../../assets/maps/map.tmx')

        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill((0, 0, 0))

            # RENDER YOUR GAME HERE
            tile_map.render(screen)

            # flip() the display to put your work on screen
            pygame.display.flip()

            clock.tick(60)  # limits FPS to 60

        pygame.quit()
