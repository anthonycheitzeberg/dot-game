import pytmx
import pygame
from src.shared import constants


class TileMap:
    def __init__(self, filename):
        self.map = pytmx.util_pygame.load_pygame(filename)
        self.width = self.map.width * self.map.tilewidth
        self.height = self.map.height * self.map.tileheight
        self.screen_width = constants.SCREEN_DIMENSIONS['WIDTH']
        self.screen_height = constants.SCREEN_DIMENSIONS['HEIGHT']

    def render(self, surface):
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    tile_rect = pygame.Rect(x * self.map.tilewidth, y * self.map.tileheight, self.map.tilewidth,
                                            self.map.tileheight)
                    surface.blit(image, tile_rect)

    def get_collision_rects(self, layer_name):
        collision = self.map.get_layer_by_name(layer_name)
        rects = []

        for x, y, tile in collision.tiles():
            if tile:
                rects.append(pygame.Rect([(x * self.map.tilewidth),
                                          (y * self.map.tileheight),
                                          self.map.tilewidth,
                                          self.map.tileheight]))
        return rects
