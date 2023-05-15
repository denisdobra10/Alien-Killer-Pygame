import pygame
from variables import bullet_attack_sfx, no_ammo_sfx, reload_sfx, upgrade_sfx

def check_events(game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False
        elif event.type == pygame.KEYDOWN:  # Check if certain key was pressed (NOT HELD)
            if event.key == pygame.K_j:
                reload_gun(game)
            if event.key == pygame.K_u:
                upgrade_speed(game)
        elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    bullet_attack(game)

    if is_key_held_down(pygame.K_a):
        move_player_to_left(game)

    if is_key_held_down(pygame.K_d):
        move_player_to_right(game)




def is_key_held_down(key):
    key_held = False

    keys = pygame.key.get_pressed()
    if keys[key]:
        if not key_held:
            return True
        key_held = True
    else:
        key_held = False


def move_player_to_left(game):
    if game.player.transform.position.x >= 0.01:
        game.player.controls.move_horizontally(-1 * game.player.moving_force.x, game.player.moving_speed.x)


def move_player_to_right(game):
    if game.player.transform.position.x <= 700.00:
        game.player.controls.move_horizontally(game.player.moving_force.x, game.player.moving_speed.x)


def reload_gun(game):
    if game.player.money >= 500:
        game.player.gun.add_ammo(10)
        game.player.money -= 500
        reload_sfx.play()


def bullet_attack(game):
    if game.player.gun.ammo > 0:
        game.player.gun.fire()
        bullet_attack_sfx.play()  # play gun shot sfx
    else:
        no_ammo_sfx.play()  # play no ammo sfx


def upgrade_speed(game):
    if game.player.money >= 1000:
        game.player.upgrade_moving_speed()
        game.player.money -= 1000
        upgrade_sfx.play()
    else:
        no_ammo_sfx.play()

