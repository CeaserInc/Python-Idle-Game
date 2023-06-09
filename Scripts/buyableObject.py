import pygame
import object


class BuyableObject(object.Object):
    def __init__(self, sprite, sprites, pos, size):

        object.Object.__init__(self, sprite, sprites, pos, size)
        self.placed = False
        self.direction = 0
        self.placed = False

    def rotate(self):
        self.direction = self.direction % 360 + 90

        match self.direction/90:
            case 1:
                self.sprite = self.sprites[2]
                self.image = pygame.image.load(self.sprite)
            case 2:
                self.sprite = self.sprites[3]
                self.image = pygame.image.load(self.sprite)
            case 3:
                self.sprite = self.sprites[1]
                self.image = pygame.image.load(self.sprite)
            case _:
                self.sprite = self.sprites[0]
                self.image = pygame.image.load(self.sprite)

    def place(self):
        self.placed = True
