import pygame
from os import path

from jumpnrun.config import LANGUAGE, DATA_DIR
from jumpnrun.screens.main import MainScreen
from jumpnrun.translate import t

# FPS dont have to be so high for an UI
# higher FPS increased the CPU usage massively
FPS: int = 30


class Game:
    def __init__(self):
        """
        initialize the game
        """
        # initialize pygame
        pygame.init()
        # set the title of the window
        pygame.display.set_caption("Jumpnrun")
        # set the icon of the window
        icon = pygame.image.load(path.join(DATA_DIR, "img", "icon.png"))
        pygame.display.set_icon(icon)
        self.width: int = 1200
        self.height: int = 600
        # flags for the window
        # doublebuf and opengl improve the performance massively
        flags = pygame.RESIZABLE | pygame.DOUBLEBUF
        # create the window
        self.surface: pygame.Surface = pygame.display.set_mode(
            (self.width, self.height), flags=flags
        )
        # set language
        t.change_language(LANGUAGE)
        # set the framerate of the game
        self.clock = pygame.time.Clock()

    def run(self):
        """
        run the game
        """
        MainScreen(self.surface).run()
