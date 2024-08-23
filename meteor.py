import pygame
import random
try:
    surface = pygame.display.get_surface()
    meteorspawned = False
    firstkill = True
    id = 0

    def spawnmeteorkiller(meteors):
        global firstkill
        if not firstkill and len(meteors) > 0:
            if random.randint(0,10) > 2:
                meteors.pop(random.randint(0,len(meteors)-1))
        meteorkiller = pygame.Rect(random.randint(20,surface.get_width()-20), random.randint(200,990), 0,0).inflate(20, 20)
        print(meteorkiller)
        firstkill = False
        return meteors, meteorkiller

    def spawnmeteor(meteors):
        global x,y, meteorspeed, id, surface,meteorspawned
        id += 1
        x = random.randint(50,surface.get_width() - 50)
        y = random.randint(-100,-50)
        height = random.randint(20,300)
        width = random.randint(20,300)
        color = (random.randint(0,255),random.randint(0,255),random.randint(0,255),random.randint(0,255))
        meteorspeed = random.randint(300,500)
        meteorspawned = True
        meteors.append([
            x,
            y,
            meteorspeed,
            meteorspawned,
            id,
            color,
            width,
            height
        ])
        return meteors, meteorspawned
except Exception as e:
    print("FEHLER:" + e)