import pygame
import os
from pygame import mixer

"""
SETUP CODE
"""
# pygame setup
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.music.set_volume(0.33)

# screen setup
display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h

# choose here whether to start in resizable or full screen
screen = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN, vsync=0)
# screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync = 0) # use to begin in windowed

init_fullscreen = True # set to true if beginning in full screen

# file system setup
current_path = os.path.dirname(__file__)
icon = pygame.image.load(current_path + '/assets/imgIco.png').convert_alpha()
pygame.display.set_caption('World Conquest')
pygame.display.set_icon(icon)

btnPlay = pygame.image.load(current_path + '/assets/buttons/btnPlay.png').convert_alpha()
btnPlayHover = pygame.image.load(current_path + '/assets/buttons/btnPlayHover.png').convert_alpha()
btnSettings = pygame.image.load(current_path + '/assets/buttons/btnSettings.png').convert_alpha()
btnSettingsHover = pygame.image.load(current_path + '/assets/buttons/btnSettingsHover.png').convert_alpha()
btnAudio = pygame.image.load(current_path + '/assets/buttons/btnAudio.png').convert_alpha()
btnAudioHover = pygame.image.load(current_path + '/assets/buttons/btnAudioHover.png').convert_alpha()
btnBack = pygame.image.load(current_path + '/assets/buttons/btnBack.png').convert_alpha()
btnBackHover = pygame.image.load(current_path + '/assets/buttons/btnBackHover.png').convert_alpha()
btnExit = pygame.image.load(current_path + '/assets/buttons/btnExit.png').convert_alpha()
btnExitHover = pygame.image.load(current_path + '/assets/buttons/btnExitHover.png').convert_alpha()
btnQuit = pygame.image.load(current_path + '/assets/buttons/btnQuit.png').convert_alpha()
btnQuitHover = pygame.image.load(current_path + '/assets/buttons/btnQuitHover.png').convert_alpha()
imgLogo = pygame.image.load(current_path + '/assets/imgLogo.png').convert_alpha()
imgBackground = pygame.image.load(current_path + '/assets/imgBackground.jpg').convert()
current_background = None

clock = pygame.time.Clock()
dt = 0

"""
GAME CODE
"""

def change_music(music_path):
    mixer.music.unload()
    mixer.music.load(music_path)
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)


class FPS:
    def __init__(self):
        self.font = pygame.font.SysFont('Calibri', 32)

    def render(self, screen):
        self.text = self.font.render('FPS: ' + str(round(clock.get_fps())), True, (255, 255, 255))
        screen.blit(self.text, (0, 0))


class UI:
    """
    this variable holds the method to render the current scene
    the variable is a pointer to the actual method definitions defined below
    to change scene, set this variable to the scene's method and return out of
    the current method to switch
    """
    current_page = None

    # change this value based on the starting screen
    fullscreen = None
    # change which key activates the fullscreen and resizable screen
    fullscreen_key = pygame.K_f

    def __init__(self):
        self.font = pygame.font.SysFont('Calibri', 32)
        self.current_page = self.menu
        self.fullscreen = init_fullscreen

        # load startup music
        change_music(current_path + '/assets/music/musicMenu.mp3')

    def render(self, screen):
        """
        render all game UI required here
        """
        self.icon = pygame.transform.scale(icon, (50, 50))
        screen.blit(self.icon, (5, screen.get_height() - 55))  # offset by 5px, so it is not stuck in the bottom left

    # this the method to render the menu scene
    def menu(self):
        # the screen and running variable are defined global
        # the initialization of these variables do not exist in this scope rather outside it.
        global screen, running

        current_background = pygame.transform.scale(imgBackground, (screen.get_width(), screen.get_height()))

        while 1:
            dt = clock.tick(165) * 0.001  # limit fps to 165 in game

            screen.blit(current_background, (0, 0))

            screen.blit(imgLogo, (screen.get_width() * 0.5 - 363, 20))

            areaPlayBtn = pygame.Rect(screen.get_width() * 0.5 - 152.5, screen.get_height() * 0.5 - 47.5, 305, 95)
            screen.blit(btnPlay, (screen.get_width() * 0.5 - 152.5, screen.get_height() * 0.5 - 47.5))

            areaExitBtn = pygame.Rect(screen.get_width() * 0.5 - 152.5, screen.get_height() * 0.5 + 47.5, 305, 95)
            screen.blit(btnExit, (screen.get_width() * 0.5 - 152.5, screen.get_height() * 0.5 + 47.5))

            areaSettingsBtn = pygame.Rect(screen.get_width() - 144 - 10, 10, 144,
                                          122)  # offset 10px from the edge of the screen
            screen.blit(btnSettings, (screen.get_width() - 144 - 10, 10))

            cursor_pos = pygame.mouse.get_pos()
            if areaPlayBtn.collidepoint(cursor_pos):
                screen.blit(btnPlayHover, (screen.get_width() * 0.5 - 152.5, screen.get_height() * 0.5 - 47.5))
            elif areaExitBtn.collidepoint(cursor_pos):
                screen.blit(btnExitHover, (screen.get_width() * 0.5 - 152.5, screen.get_height() * 0.5 + 47.5))
            elif areaSettingsBtn.collidepoint(cursor_pos):
                screen.blit(btnSettingsHover, (screen.get_width() - 144 - 10, 10))

            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if areaPlayBtn.collidepoint(event.pos):
                        self.current_page = self.game
                        change_music(current_path + '/assets/music/musicBackground.mp3')
                        return
                    elif areaExitBtn.collidepoint(event.pos):
                        running = False
                        return
                    elif areaSettingsBtn.collidepoint(event.pos):
                        screen.fill("black")
                        current_background.set_alpha(60)
                        screen.blit(current_background, (0, 0))
                        pygame.display.flip()
                        """
                        ! important !
                        this lowers the opacity of the background BEFORE opening the menu
                        this means you do not need to call .set_alpha(60) on each frame
                        while in the menu, which tanks performance
                        """
                        self.current_page = self.menu_settings
                        return

                if event.type == pygame.KEYDOWN:
                    if event.key == self.fullscreen_key:
                        if self.fullscreen:
                            screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync=0)
                            current_background = pygame.transform.scale(imgBackground, (screen.get_width(), screen.get_height()))
                            self.fullscreen = False
                        else:
                            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=0)
                            current_background = pygame.transform.scale(imgBackground, (screen.get_width(), screen.get_height()))
                            self.fullscreen = True
                    if event.key == pygame.K_ESCAPE:
                        screen.fill("black")
                        current_background.set_alpha(60)
                        screen.blit(current_background, (0, 0))
                        pygame.display.flip()
                        """
                        ! important !
                        this lowers the opacity of the background BEFORE opening the menu
                        this means you do not need to call .set_alpha(60) on each frame
                        while in the menu, which tanks performance
                        """
                        self.current_page = self.menu_settings
                        return

            # fps.render(screen) # uncomment for debugging
            pygame.display.flip()

    def menu_settings(self):
        global screen, running

        while 1:
            dt = clock.tick(165) * 0.001  # limit fps to 165 in game

            areaAudioBtn = pygame.Rect(screen.get_width() - 289 - 15, 132, 289, 90)
            screen.blit(btnAudio, (screen.get_width() - 289 - 15, 132))

            areaBackBtn = pygame.Rect(screen.get_width() - 289 - 15, 230, 289, 90)
            screen.blit(btnBack, (screen.get_width() - 289 - 15, 230))

            areaSettingsBtn = pygame.Rect(screen.get_width() - 144 - 10, 10, 144,
                                          122)  # offset 10px from the edge of the screen
            screen.blit(btnSettings, (screen.get_width() - 144 - 10, 10))

            cursor_pos = pygame.mouse.get_pos()
            if areaAudioBtn.collidepoint(cursor_pos):
                screen.blit(btnAudioHover, (screen.get_width() - 289 - 15, 132))
            elif areaBackBtn.collidepoint(cursor_pos):
                screen.blit(btnBackHover, (screen.get_width() - 289 - 15, 230))
            elif areaSettingsBtn.collidepoint(cursor_pos):
                screen.blit(btnSettingsHover, (screen.get_width() - 144 - 10, 10))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if areaAudioBtn.collidepoint(event.pos):
                        volume = mixer.music.get_volume()
                        if volume > 0:
                            mixer.music.set_volume(0)
                        else:
                            mixer.music.set_volume(0.33)
                        return
                    if areaBackBtn.collidepoint(event.pos) or areaSettingsBtn.collidepoint(event.pos):
                        self.current_page = self.menu
                        return

                if event.type == pygame.KEYDOWN:
                    if event.key == self.fullscreen_key:
                        if self.fullscreen:
                            screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync=0)
                            current_background = pygame.transform.scale(imgBackground, (screen.get_width(), screen.get_height()))
                            current_background.set_alpha(60)
                            screen.blit(current_background, (0, 0))
                            pygame.display.flip()
                            """
                            ! important !
                            this lowers the opacity of the background BEFORE fullscreen
                            this means you do not need to call .set_alpha(60) on each frame
                            while in the menu, which tanks performance
                            """
                            self.fullscreen = False
                        else:
                            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=0)
                            current_background = pygame.transform.scale(imgBackground, (screen.get_width(), screen.get_height()))
                            current_background.set_alpha(60)
                            screen.blit(current_background, (0, 0))
                            pygame.display.flip()
                            """
                            ! important !
                            this lowers the opacity of the background BEFORE fullscreen
                            this means you do not need to call .set_alpha(60) on each frame
                            while in the menu, which tanks performance
                            """
                            self.fullscreen = True

            """
            render only the button area, to improve performance and reduce unnecessary rendering
            """
            # pygame.draw.rect(screen, (0, 0, 0, 255), pygame.Rect(0, 0, 100, 25))  # prevents FPS values overlapping
            # fps.render(screen) # uncomment for debugging
            pygame.display.update(pygame.Rect(0, 0, 100, 25))
            pygame.display.update(pygame.Rect(screen.get_width() - 289 - 10, 0, 304, 332))

    def game(self):
        global running, screen

        c1 = pygame.image.load(current_path + '/assets/countries/country1.png').convert_alpha()
        c2 = pygame.image.load(current_path + '/assets/countries/country2.png').convert_alpha()

        while 1:
            screen.fill("black")
            dt = clock.tick(165) * 0.001  # limit fps to 165 in game

            # insert game logic here

            c1_pos = (100, 200)
            c1_mask = pygame.mask.from_surface(c1)
            screen.blit(c1, c1_pos)

            c2_pos = (500, 400)
            c2_mask = pygame.mask.from_surface(c2)
            screen.blit(c2, c2_pos)

            areaSettingsBtn = pygame.Rect(screen.get_width() - 144 - 10, 10, 144,
                                          122)  # offset 10px from the edge of the screen
            screen.blit(btnSettings, (screen.get_width() - 144 - 10, 10))

            cursor_pos = pygame.mouse.get_pos()
            if areaSettingsBtn.collidepoint(cursor_pos):
                screen.blit(btnSettingsHover, (screen.get_width() - 144 - 10, 10))

            keys = pygame.key.get_pressed()

            fps.render(screen)
            ui.render(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    """
                    if you are reading this i apologise in advance
                    there must be about 50 better ways of doing
                    the exact same thing
                    """
                    try:
                        if c1_mask.get_at((event.pos[0] - c1_pos[0], event.pos[1] - c1_pos[1])):
                            print('clicked {country 1}')
                    except IndexError:
                        pass # ignore the exception :skull: :skull:

                    try:
                        if c2_mask.get_at((event.pos[0] - c2_pos[0], event.pos[1] - c2_pos[1])):
                            print('clicked {country 2}')
                    except IndexError:
                        pass # ignore the exception :skull: :skull:

                    if areaSettingsBtn.collidepoint(event.pos):
                            self.current_page = self.game_settings
                            return

                if event.type == pygame.KEYDOWN:
                    if event.key == self.fullscreen_key:
                        if self.fullscreen:
                            screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync=0)
                            self.fullscreen = False
                        else:
                            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=0)
                            self.fullscreen = True
                
                    if event.key == pygame.K_ESCAPE:
                        self.current_page = self.game_settings
                        return

            pygame.display.flip()
    
    def game_settings(self):
        global screen, running

        while 1:
            dt = clock.tick(165) * 0.001  # limit fps to 165 in game

            areaAudioBtn = pygame.Rect(screen.get_width() - 289 - 15, 132, 289, 90)
            screen.blit(btnAudio, (screen.get_width() - 289 - 15, 132))

            areaQuitBtn = pygame.Rect(screen.get_width() - 289 - 15, 230, 289, 90)
            screen.blit(btnQuit, (screen.get_width() - 289 - 15, 230))

            areaSettingsBtn = pygame.Rect(screen.get_width() - 144 - 10, 10, 144, 122)  # offset 10px from the edge of the screen
            screen.blit(btnSettings, (screen.get_width() - 144 - 10, 10))


            cursor_pos = pygame.mouse.get_pos()
            if areaAudioBtn.collidepoint(cursor_pos):
                screen.blit(btnAudioHover, (screen.get_width() - 289 - 15, 132))
            elif areaQuitBtn.collidepoint(cursor_pos):
                screen.blit(btnQuitHover, (screen.get_width() - 289 - 15, 230))
            elif areaSettingsBtn.collidepoint(cursor_pos):
                screen.blit(btnSettingsHover, (screen.get_width() - 144 - 10, 10))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if areaAudioBtn.collidepoint(event.pos):
                        volume = mixer.music.get_volume()
                        if volume > 0:
                            mixer.music.set_volume(0)
                        else:
                            mixer.music.set_volume(0.33)
                        return
                    if areaQuitBtn.collidepoint(event.pos):
                        self.current_page = self.menu
                        # load menu music
                        change_music(current_path + '/assets/music/musicMenu.mp3')
                        return
                    if areaSettingsBtn.collidepoint(event.pos):
                        self.current_page = self.game
                        return

                if event.type == pygame.KEYDOWN:
                    if event.key == self.fullscreen_key:
                        if self.fullscreen:
                            screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE, vsync=0)
                            self.fullscreen = False
                        else:
                            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN, vsync=0)
                            self.fullscreen = True

            """
            render only the button area, to improve performance and reduce unnecessary rendering
            """
            # pygame.draw.rect(screen, (0, 0, 0, 255), pygame.Rect(0, 0, 100, 25))  # prevents FPS values overlapping
            # fps.render(screen) # uncomment for debugging
            # pygame.display.update(pygame.Rect(0, 0, 100, 25))
            pygame.display.update(pygame.Rect(screen.get_width() - 289 - 10, 0, 304, 332))


fps = FPS()
ui = UI()
running = True
while running:
    ui.current_page()

print("quitting python")
pygame.quit()
quit()
