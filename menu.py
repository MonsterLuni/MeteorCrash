import pygame
try:
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1000,1000))
    running = False
    surface = pygame.display.get_surface()
    screen_fullscreen = pygame.display.get_desktop_sizes()
    player_pos = pygame.Vector2(surface.get_width() / 2, surface.get_height() / 2)
    fullscreen = False
    dt = 0

    def togglefullscreen():
            global fullscreen, screen_height, surface

            match fullscreen:
                case False:
                    pygame.display.set_mode(screen_fullscreen[0])
                    fullscreen = True
                    pygame.display.toggle_fullscreen()
                case True:
                    pygame.display.toggle_fullscreen()
                    pygame.display.set_mode((1000,1000))
                    fullscreen = False
                    screen_height = 1000    
            surface = pygame.display.get_surface()
            player_pos.x = surface.get_width() / 2
            return pygame.display.get_surface(), player_pos.x

    def menu(playing):
        global running, dt, surface
        while playing:
            dt = clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    #Hier schaut es, auf welche Farbe man geklickt hat.
                    color = pygame.Surface.get_at(screen,(mouse_pos[0],mouse_pos[1]))
                    if color == (0,0,255,255):
                        surface, player_pos.x = togglefullscreen()
                    if color == (0,255,0,255): 
                        playing = False
                keys = pygame.key.get_pressed()
                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_ESCAPE]:
                        playing = False
                    if keys[pygame.K_F11]:
                        surface, player_pos.x = togglefullscreen()

            screen.fill((11,11,11,255))

            pygame.draw.circle(screen,"blue",(screen.get_width()-30,30),20)

            Begin = pygame.draw.circle(screen,"green",(screen.get_width() / 2, screen.get_height() / 2 +80),20)

            pygame.display.flip()
        return surface, True, player_pos.x
except Exception as e:
    print("FEHLER:" + e)