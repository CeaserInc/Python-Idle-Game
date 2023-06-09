import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, sprite, sprites, pos, size):

        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.num = sprite
        self.sprites = sprites
        self.sprite = sprites[sprite - 1]
        self.rect = pygame.Rect(pos.x, pos.y, size.x, size.y)
        self.image = pygame.image.load(self.sprite)

    def move(self, pos):
        self.pos.x = pos.x
        self.pos.y = pos.y

    def update(self):
        self.rect.topleft = self.pos.x, self.pos.y

    def isTouching(self, objectGroup):
        return len(pygame.sprite.spritecollide(self, objectGroup, False)) > 1

    def getTouching(self, objectGroup):
        return pygame.sprite.spritecollide(self, objectGroup, False)
