import os
import buyableObject

conveyor_sprites = []

for conveyorFolder in os.listdir("../Sprites/Conveyors"):
    for conveyor in os.listdir('../Sprites/Conveyors/' + conveyorFolder):
        conveyor_sprites.append(os.path.abspath(
            "../Sprites/Conveyors/" + conveyorFolder + '/' + conveyor))


class Conveyor(buyableObject.BuyableObject):
    def __init__(self, sprite, pos, size):
        buyableObject.BuyableObject.__init__(
            self, sprite, conveyor_sprites, pos, size)
