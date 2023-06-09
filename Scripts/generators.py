import os
import buyableObject
import ores
from vector2 import Vector2

generator_sprites = []

for generatorFolder in os.listdir('../Sprites/Generators/'):
    for generator in os.listdir('../Sprites/Generators/' + generatorFolder):
        generator_sprites.append(os.path.abspath(
            '../Sprites/Generators/' + generatorFolder + '/' + generator))


class Generator(buyableObject.BuyableObject):
    def __init__(self, sprite, pos, size):
        buyableObject.BuyableObject.__init__(
            self, sprite, generator_sprites, pos, size)

    def makeOre(self):
        if self.placed:
            product = None
            ORE_SIZE = Vector2(10, 10)
            match self.direction % 360:
                case 180:
                    product = ores.Ore(
                        self.num, Vector2(self.rect.x+14, self.rect.y-7), ORE_SIZE)
                    return product
                case 270:
                    product = ores.Ore(
                        self.num, Vector2(self.rect.x-35, self.rect.y+14), ORE_SIZE)
                    return product
                case 90:
                    product = ores.Ore(
                        self.num, Vector2(self.rect.x+35, self.rect.y+14), ORE_SIZE)
                    return product
                case 0:
                    product = ores.Ore(
                        self.num, Vector2(self.rect.x + 14, self.rect.y + 35), ORE_SIZE)
                    return product
        return None
