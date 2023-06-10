import pygame
import conveyors
import generators
import ores
from vector2 import Vector2
import math

WIDTH = 360
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

GENERATOR_SIZE = Vector2(30, 30)
CONVEYOR_SIZE = Vector2(30, 30)
GRID_SPACING = 30


def main():
    global screen, clock, allObjectsGroup, currentlyPlacing, buyMode
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("<Your game>")
    clock = pygame.time.Clock()

    currentlyPlacing = False

    allObjectsGroup = pygame.sprite.Group()

    buyMode = 'c'

    gameLoop()


def gameLoop():
    global allObjectsGroup, currentlyPlacing, screen

    frame = 0
    running = True
    while running:

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                controls(chr(event.key))
            if event.type == pygame.MOUSEBUTTONDOWN:
                controls('', pygame.mouse.get_pressed())

        if frame % 30 == 0:
            objects = getObject(allObjectsGroup, [generators.Generator], True)
            for object in objects:
                newOre = object.makeOre()
                if newOre != None:
                    allObjectsGroup.add(newOre)

        allObjectsGroup.update()

        screen.fill(BLACK)

        moveBuyableObject()
        conveyorMove()
        killOreOnGround()

        allObjectsGroup.draw(screen)

        pygame.display.flip()

        frame += 1

    pygame.quit()


def controls(key, mouse=()):
    global currentlyPlacing, buyMode, allObjectsGroup
    if key != '':
        if key.lower() in 'cg':
            buyMode = key.lower()
        if key in '123456789' and type(currentlyPlacing) == bool:
            buy(int(key))
        elif key == 'r' and type(currentlyPlacing) != bool:
            currentlyPlacing.rotate()
    elif mouse != ():
        if mouse[0] == True and currentlyPlacing:
            if not (currentlyPlacing.isTouching(getObject(allObjectsGroup, [generators.Generator, conveyors.Conveyor], True))):
                currentlyPlacing.place()
                currentlyPlacing = False


def buy(key):
    global currentlyPlacing, buyMode
    if buyMode == 'c':
        currentlyPlacing = conveyors.Conveyor(
            key, gridMousePos(pygame.mouse.get_pos()), CONVEYOR_SIZE)
        allObjectsGroup.add(currentlyPlacing)
    elif buyMode == 'g':
        currentlyPlacing = generators.Generator(
            key, gridMousePos(pygame.mouse.get_pos()), GENERATOR_SIZE)
        allObjectsGroup.add(currentlyPlacing)


def moveBuyableObject():
    global currentlyPlacing
    if currentlyPlacing:
        if not (currentlyPlacing.placed):
            currentlyPlacing.move(gridMousePos(pygame.mouse.get_pos()))


def conveyorMove():
    global allObjectsGroup
    conveyorList = getObject(allObjectsGroup, [conveyors.Conveyor], True)
    oreList = getObject(allObjectsGroup, [ores.Ore])
    for ore in oreList:
        ore.changeVelocity(conveyorList)


def getObject(group, objectTypes, needPlaced=False):
    objects = []
    for item in group.sprites():
        if type(item) in objectTypes:
            if needPlaced:
                if item.placed:
                    objects.append(item)
            else:
                objects.append(item)
    return objects


def gridMousePos(pos):
    global GRID_SPACING
    return Vector2(math.floor(pos[0] / GRID_SPACING) * GRID_SPACING, math.floor(pos[1] / GRID_SPACING) * GRID_SPACING)

def killOreOnGround():
    global allObjectsGroup
    oreList = getObject(allObjectsGroup, [ores.Ore])
    collisions = []
    for ore in oreList:
        collisions = pygame.sprite.spritecollide(ore, allObjectsGroup, False)
        if len(collisions) == 1:
            ore.kill()
            print("1")
        elif len(collisions) == 2:
            if type(collisions[0]) == ores.Ore:
                ore.kill()
                print("2")
            elif not(collisions[0].placed):
                ore.kill()
                print("3")

if __name__ == "__main__":
    main()
