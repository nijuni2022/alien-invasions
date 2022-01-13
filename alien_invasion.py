import pygame
from settings import Settings
from ship import Ship

import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():

    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(ai_settings, screen,"Play")
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)

    bullets = Group()
    aliens = Group()

    bg_color = (230, 230, 230)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.mixer.music.load('sounds/star_wars.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play(-1)

    while True:

        gf.check_events( ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:

            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        # gf.update_aliens(ai_settings, aliens)
        # ship.update()
        # gf.update_bullets(ai_settings, screen, ship, bullets)

        # gf.check_events(ai_settings, screen, ship, aliens)



if __name__ == "__main__":
    run_game()
