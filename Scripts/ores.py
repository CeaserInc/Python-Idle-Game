import object
import os
from vector2 import Vector2

ore_sprites = []

for oreFolder in os.listdir('../Sprites/Ores/'):
    for ore in os.listdir('../Sprites/Ores/' + oreFolder):
        ore_sprites.append(os.path.abspath(
            '../Sprites/Ores/' + oreFolder + '/' + ore))


class Ore(object.Object):
    def __init__(self, sprite, initialPos, size):
        object.Object.__init__(self, sprite, ore_sprites, initialPos, size)
        self.velocity = Vector2(0, 0)
        self.maxSpeed = 0
        self.friction = Vector2(1 - 99/3000, 1 - 99/3000)

    def changeVelocity(self, objects):
        conveyors = self.getTouching(objects)
        if len(conveyors) > 0:
            direction = conveyors[0].direction
            speed = conveyors[0].num + 1
            match direction % 360:
                case 0:
                    self.velocity.transform(Vector2(0, speed), "add")
                case 90:
                    self.velocity.transform(Vector2(speed, 0), "add")
                case 180:
                    self.velocity.transform(Vector2(0, -speed), "add")
                case 270:
                    self.velocity.transform(Vector2(-speed, 0), "add")
            self.maxSpeed = conveyors[0].num + 1

    def useFriction(self):
        self.velocity.transform(self.friction, "multiply")
        if self.velocity.x < 0.01:
            self.velocity.x = 0
        elif self.velocity.x > self.maxSpeed:
            self.velocity.x = self.maxSpeed
        if self.velocity.y < 0.01:
            self.velocity.y = 0
        elif self.velocity.y > self.maxSpeed:
            self.velocity.y = self.maxSpeed

    def move(self):
        self.pos.transform(self.velocity, "add")
        self.useFriction()

    def update(self):
        self.move()

        return super().update()
