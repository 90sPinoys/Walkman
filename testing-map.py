#Import statements are to enable the code to use the functions from the library
from pytmx.util_pygame import load_pygame
import pytmx
import pygame
import sys
import os

#initialize pygame & window
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
SCREENWIDTH = 500
SCREENHEIGHT = 500
SCREENSIZE = [SCREENWIDTH, SCREENHEIGHT]
SCREEN = pygame.display.set_mode(SCREENSIZE)

tiled_map = load_pygame('untitled.tmx')
tilewidth = tiled_map.tilewidth
tileheight = tiled_map.tileheight
collision = tiled_map.get_layer_by_name('Tile Layer 1')

#caption for the game
pygame.display.set_caption("My first game in pygame")

#game loop
while True:
    for events in pygame.event.get():  # get all pygame events
        if events.type == pygame.QUIT:  # if event is quit then shutdown window and program
            pygame.quit()
            sys.exit()
    for layer in tiled_map.layers:
        if isinstance(layer, pytmx.TiledTileLayer):
            for x, y, tile in layer.tiles():
                if (tile):
                    SCREEN.blit(tile, [x*tilewidth, y*tileheight])

        elif isinstance(layer, pytmx.TiledObjectGroup):
            for object in layer:
                if (object.type == 'Player'):
                    SCREEN.blit(player, (object.x, object.y))

    
    pygame.display.update()

