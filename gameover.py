import pygame
import mysql.connector
import json

pygame.font.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,1000))
input_box = pygame.Rect(100, 100, 140, 32)
txt_surfaceColor = "green"
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
fullscreen = False
font = pygame.font.Font(None, 32)
dt = 0
text = ''

def gameover(score, gameover, starttime, endtime, won):
    global dt, text, color, active
    while gameover:
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(1).stop()
        #Hier wird die Framerate auf 10 gesetzt, um Ressourcen zu sparen
        dt = clock.tick(10) / 1000
        #Jeder Frame wird überschrieben mit Schwarz, das man immer nur das aktuelle sieht.
        screen.fill("black")
        font = pygame.font.SysFont(None, 80)
        Score = font.render(str(score / 10), True, "red")
        Game_Over = font.render("Game Over", True, "white")
        screen.blit(Game_Over, ((screen.get_width() / 2) - 150,screen.get_height() / 2))
        screen.blit(Score, ((20,20)))
        End = pygame.draw.circle(screen,"green",(screen.get_width() / 2, screen.get_height() / 2 +80),20)

        txt_surface = font.render(text, True, txt_surfaceColor)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        
        for event in pygame.event.get():
            #Das event .quit ist, wenn ein User auf das X drückt
            if event.type == pygame.QUIT:
                gameover = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                color = pygame.Surface.get_at(screen,(mouse_pos[0],mouse_pos[1]))
                if color == (0,255,0,255):
                    gameover = False

                if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active     
                else:
                    active = False
                    # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    gameover = False
                if active:
                    if event.key == pygame.K_RETURN:
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                else:
                    if keys[pygame.K_s]:
                        save(score, starttime, endtime, won, gameover)

        pygame.display.flip()

def win(score, gameover, starttime, endtime, won):
    global dt, text, color, active, font
    while won:
        pygame.mixer.Channel(0).stop()
        pygame.mixer.Channel(1).stop()
        #Hier wird die Framerate auf 10 gesetzt, um Ressourcen zu sparen
        dt = clock.tick(10) / 1000
        #Jeder Frame wird überschrieben mit Schwarz, das man immer nur das aktuelle sieht.
        screen.fill("black")
        Game_Won = font.render("Won!", True, "white")
        Score = font.render(str(score / 10), True, "red")
        screen.blit(Game_Won, ((screen.get_width() / 2) - 150,screen.get_height() / 2))
        screen.blit(Score, ((20,20)))
        End = pygame.draw.circle(screen,"green",(screen.get_width() / 2, screen.get_height() / 2 +80),20)

        txt_surface = font.render(text, True, txt_surfaceColor)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)
        
        for event in pygame.event.get():
            #Das event .quit ist, wenn ein User auf das X drückt
            if event.type == pygame.QUIT:
                won = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                color = pygame.Surface.get_at(screen,(mouse_pos[0],mouse_pos[1]))
                if color == (0,255,0,255):
                    won = False

                if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active     
                else:
                    active = False
                    # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    won = False
                if active:
                    if event.key == pygame.K_RETURN:
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                else:
                    if keys[pygame.K_s]:
                        save(score, starttime, endtime, won, gameover)
        pygame.display.flip()
    return False

def save(score, starttime, endtime, win, gameover):
    global savefile, text, time, txt_surfaceColor, fullscreen

    my_list = ['drop', 'database', 'table', 'insert', '(', ')', '"']

    if any(substring in text for substring in my_list):
        print("Name ist ungültig")
        txt_surfaceColor = "red"
    else:
        Database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="meteorcrash"
        )

        if win:
            time = 216

        meteorsspawned = int(((score/10)/20) + 1)

        time = (endtime - starttime)/1000
        
        mycursor = Database.cursor()

        sql = "INSERT INTO records (name, score, meteorsspawned, fullscreen, time, won) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (text, score/10, meteorsspawned, fullscreen, time, win)
        
        mycursor.execute(sql, val)

        Database.commit()

        #Liest die Datei, sodass keine Daten verloren gehen.
        with open("./MeteorCrash with Classes/savefile.json", mode='r') as f:
            savefile = json.load(f)
        
        #Schreibt das ganze Array auf die Datei
        record = {"name": text, "record": score/10, "meteorsspawned": meteorsspawned, "fullscreen": fullscreen, "time": time, "won": win}
        with open("./MeteorCrash with Classes/savefile.json", mode='w') as f:
            savefile.append(record)
            json.dump(savefile, f, indent=2)
        