import pygame
import random
import menu as menupage
import gameover as gm
import meteor as m
import function as f
#pygame muss Installiert sein um das Projekt abspielen zu können!
#Um es zu installieren: "pip install pygame"
#mysql.connector auch

#Um Pygame zu initialisieren
pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Meteor Crash')

screen = pygame.display.set_mode((1000,1000))
screen_fullscreen = pygame.display.get_desktop_sizes()
clock = pygame.time.Clock()
surface = pygame.display.get_surface()
player_pos = pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2)
sysfont = pygame.font.get_default_font()
pygame.mixer.Channel(0).set_volume(0.4)
pygame.mixer.Channel(1).set_volume(0.6)
pygame.mixer.Channel(2).set_volume(0.4)
pygame.mixer.Channel(3).set_volume(0.4)

win = False
menu = True
running = False
dt = 0
score = 0
fullscreen = False
screen_height = 1000
gameover = False
stopper = 0
ticksnow = 0
meteorspawned = False
id = 0
savefile = []
soundplaying = False
firsttime = True
firsttime2 = True
dead = False
starttime = 0
endtime = 0
firstkill = True
txt_surfaceColor = "green"
speedup = 500
speedhorizontal = 800
firstpowerup = True
meteors = []
meteorkillerposition = 0

meteors, meteorspawned = m.spawnmeteor(meteors)
meteors, meteorkillerposition = m.spawnmeteorkiller(meteors)
powerup, speedup, speedhorizontal = f.spawnpowerup(speedup, speedhorizontal)

def main():
    global dt, score, firsttime, win, running, dead, Game_Over, Game_Won, endtime, gameover, firsttime2, meteors, meteorkillerposition, meteorspawned, ticksnow, player_pos, powerup, speedup, speedhorizontal
    while running:
        print(surface)
        dt = clock.tick(60) / 1000

        player_pos.y += 450 * dt
        time = (pygame.time.get_ticks() - starttime)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = False
                running = False
        screen.fill((score / 150,0,0,255))
        font = pygame.font.SysFont(None, 80)

        Score = font.render(str(score / 10) + " Parsec", True, "red")
        player = pygame.draw.circle(screen,"red",player_pos,10)
        if fullscreen == True:
            player = pygame.draw.circle(screen,"black",(surface.get_width()/2,surface.get_height()/2),300)

        
        for meteor in meteors:
            meteor[1] += meteor[2] * dt
            meteor[4] = pygame.Rect((meteor[0] % surface.get_width() - 50),meteor[1], 0, 0).inflate(meteor[6], meteor[7])
            collide = meteor[4].collidepoint(player_pos)
            color = (255, 0, 0) if collide else (meteor[5])
            pygame.draw.rect(screen, color, meteor[4])
            if collide:
                dead = True 
            if meteor[1] > surface.get_height()-100:
                meteor[0] = random.randint(50,surface.get_width() - 50)
                meteor[2] = random.randint(300,1000)
                meteor[1] = random.randint(-100,-50)

        pygame.draw.line(screen, "red", (0,surface.get_height()-100),(surface.get_width(),surface.get_height()-100),5)

        collidekiller = meteorkillerposition.collidepoint(player_pos)
        colorkiller = (255, 0, 0) if collidekiller else (255,215,0)
        if collidekiller:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("./MeteorCrash/assets/music/meteor.mp3"))
            meteors, meteorkillerposition = m.spawnmeteorkiller(meteors)
        pygame.draw.rect(screen, colorkiller, meteorkillerposition)

        collidepowerup = powerup.collidepoint(player_pos)
        colorpowerup = (255, 0, 0) if collidekiller else (0,255,0)
        if collidepowerup:
            pygame.mixer.Channel(3).play(pygame.mixer.Sound("./MeteorCrash/assets/music/powerup.mp3"))
            powerup, speedup, speedhorizontal = f.spawnpowerup(speedup, speedhorizontal)
        pygame.draw.rect(screen, colorpowerup,  powerup)

        screen.blit(Score, (20,20))
        
        if player_pos.y > surface.get_height()-100 or player_pos.y < 0 or player_pos.x < 0 or player_pos.x > surface.get_width():
            running = False
            gameover = True
            endtime = pygame.time.get_ticks()
        if player_pos.y > 800:
            if firsttime2 == True:
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("./MeteorCrash/assets/music/Emergency.mp3"))
                firsttime2 = False
        else:
            firsttime2 = True
            pygame.mixer.Channel(0).stop()
            if firsttime == True:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("./MeteorCrash/assets/music/Annihilate.mp3"))
                firsttime = False
            else:
                pygame.mixer.Channel(1).unpause()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= speedup * dt
            score += 1
            if (score/10 % 20) == 0:
                print("Du befindest dich " + str(score/10) + " Parsecs weit weg")
                meteors, meteorspawned = m.spawnmeteor(meteors)
        if keys[pygame.K_a]:
            player_pos.x -= speedhorizontal * dt
        if keys[pygame.K_s]:
            player_pos.y += 600 * dt
        if keys[pygame.K_d]:
            player_pos.x += speedhorizontal * dt
        if keys[pygame.K_ESCAPE]:
            running = False
            gameover = True
            endtime = pygame.time.get_ticks()
        if keys[pygame.K_DELETE]:
            print("DELETE")
            gameover, score, player_pos, ticksnow, meteors, meteorspawned = f.respawn(gameover, score, player_pos, ticksnow, meteors, meteorspawned)
            meteors, meteorspawned = m.spawnmeteor(meteors)
            

        pygame.display.flip()

        if dead:
            endtime = pygame.time.get_ticks()
            running = False
            gameover = True
            pygame.time.wait(200)
        if time > 213:
            endtime = pygame.time.get_ticks()
            running = False
            gameover = True
            win = True
            pygame.time.wait(200)

if menu:
    surface, running, player_pos.x = menupage.menu(menu)

if gameover:
    if win:
        gameover, win = gm.win(score, gameover, starttime, endtime, True)
    else:
        gameover, win = gm.gameover(score, gameover, starttime, endtime, False)

if running:
    main()
pygame.font.quit()
pygame.mixer.quit()
pygame.quit()