import pygame
import random
try:
    surface = pygame.display.get_surface()
    firstpowerup = True

    def respawn(gameover, score, player_pos, ticksnow, meteors, meteorspawned):
        global surface
        ticksnow = pygame.time.get_ticks()
        gameover = False
        score = 0
        meteors = []
        player_pos = pygame.Vector2(surface.get_width() / 2, 200)
        return gameover, score, player_pos, ticksnow, meteors, meteorspawned

    def spawnpowerup(speedup,speedhorizontal):
        global powerup, firstpowerup
        if not firstpowerup:
            speedup += 10
            speedhorizontal += 10
        powerup = pygame.Rect(random.randint(20,surface.get_width()-20), random.randint(200,990), 0,0).inflate(20, 20)
        firstpowerup = False
        return powerup, speedup, speedhorizontal
except Exception as e:
    print("FEHLER:" + e)