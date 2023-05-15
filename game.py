from scripts.gameengine import *
from scripts.gamemanager import *
from scripts.enemy import Enemy
import pygame
from variables import *
import time
import random


# Create player
player = Player()
playerImg = pygame.transform.scale(playerImg, (player.transform.localScale.x, player.transform.localScale.y))
player.set_position(playerInitPos)
player.setup_moving(Vector2(2, 1), Vector2(0.15, 0.1))
player.money = 500

# Create game
game = Game(player)

score = 0
highscore = 0

def render_text_on_screen(text_content: str, text_color_rgb, text_size: int, position: Vector2):
    font = pygame.font.Font(None, 36)  # Choose a font and font size
    text_surface = font.render(text_content, True, text_color_rgb)  # Render the text with white color
    screen.blit(text_surface, (position.x, position.y)) 


def display_player_on_screen():
    screen.blit(playerImg, (player.transform.position.x, player.transform.position.y))  # Render player


def display_ammo_on_screen():
    screen.blit(ammoImg, (AMMO_IMG_POS.x, AMMO_IMG_POS.y))  # Render ammo
    render_text_on_screen(str(game.player.gun.ammo), (255, 255, 255), 20, AMMO_TEXT_POS)


def display_money_on_screen():
    ScreenOptions.render_image_on_screen(screen, dollarImg, DOLLAR_IMG_POS)
    ScreenOptions.render_text_on_screen(screen, str(game.player.money), (255, 255, 255), 40, MONEY_TEXT_POS)


timer_between_smaller_aliens = True
def resolve_bullets_movement():
    global score
    global highscore
    global timer_between_smaller_aliens

    for bullet in player.gun.bullets_shot:
        ScreenOptions.render_image_on_screen(screen, bulletImg, bullet.position)

        if bullet.position.y > -20:
            bullet.move()
        else:
            player.gun.bullets_shot.remove(bullet)

        # Check collision with enemies
        for enemy in game.enemies:
            if bullet_collision(bullet, enemy):
                game.player.money += enemy.money
                game.enemies.remove(enemy)
                explosion_sfx.play()
                score += 1
                if score > int(highscore):
                    highscore = score
                
                # chance to spawn 1 to 3 small enemies
                if random.randint(1, 3) == 1 and timer_between_smaller_aliens is True:
                    random_x = 0
                    random_y = 0

                    if(random.randint(1, 2) == 1):
                        random_x = enemy.transform.position.x - random.randint(100, random.randint(101, 150))

                        if(random.randint(1, 2) == 1):
                            random_y = enemy.transform.position.y - random.randint(20, random.randint(21, 40))
                        else:
                            random_y = enemy.transform.position.y + random.randint(20, random.randint(21, 40))
                    else:
                        random_x = enemy.transform.position.x + random.randint(100, random.randint(101, 150))

                        if(random.randint(1, 2) == 1):
                            random_y = enemy.transform.position.y - random.randint(20, random.randint(21, 40))
                        else:
                            random_y = enemy.transform.position.y + random.randint(20, random.randint(21, 40))


                    spawn_pos = Vector2(random_x, random_y)
                    game.enemies.append(Enemy(False, spawn_pos))
                    timer_between_smaller_aliens = False



def resolve_enemies_movement():
    for enemy in game.enemies:
        if enemy.big_enemy is True:
            ScreenOptions.render_image_on_screen(screen, alienImg, enemy.transform.position)
        else:
            ScreenOptions.render_image_on_screen(screen, smallerAlienImg, enemy.transform.position)

        if enemy.transform.position.x >= 700:
            enemy.direction = "left"
        elif enemy.transform.position.x <= 0:
            enemy.direction = "right"

        if "right" in enemy.direction:
            enemy.move_horizontally(True)
        else:
            enemy.move_horizontally(False)

        enemy.move_vertically()

        # Check collision with player
        if player_collision(enemy, player):
            game.running = False


def bullet_collision(bullet, enemy):
    bullet_rect = pygame.Rect(bullet.position.x, bullet.position.y, bulletImg.get_width(), bulletImg.get_height())
    enemy_rect = pygame.Rect(enemy.transform.position.x, enemy.transform.position.y, alienImg.get_width(), alienImg.get_height())
    return bullet_rect.colliderect(enemy_rect)


def player_collision(enemy, player):
    enemy_rect = pygame.Rect(enemy.transform.position.x, enemy.transform.position.y, alienImg.get_width(), alienImg.get_height())
    player_rect = pygame.Rect(player.transform.position.x, player.transform.position.y, playerImg.get_width(), playerImg.get_height())
    return enemy_rect.colliderect(player_rect)



start_time = time.time()
spawn_after = random.randint(1, 7)
def enemy_spawner():
    global start_time  
    global spawn_after
    global score
    global timer_between_smaller_aliens

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Check if 5 second have passed
    if elapsed_time >= spawn_after:
        game.enemy_spawner.spawn_enemy(True)
        timer_between_smaller_aliens = True
        start_time = time.time()

        if score > 5:
            spawn_after = random.randint(1, 6)
        elif score > 15:
            spawn_after = random.randint(1, 5)
        elif score > 30:
            spawn_after = random.randint(1, 4)
        elif score > 50:
            spawn_after = random.randint(1, 3)
        elif score > 75:
            spawn_after = random.randint(1, 2)
        elif score > 100:
            spawn_after = random.randint(1, 2)



def help_message():
    ScreenOptions.render_text_on_screen(screen, f"Score: {score}", (167, 255, 120), 30, Vector2(350, 20))

    if score > int(highscore):
        ScreenOptions.render_text_on_screen(screen, f"Highscore: {score}", (167, 255, 120), 25, Vector2(340, 50))
    else:
        ScreenOptions.render_text_on_screen(screen, f"Highscore: {highscore}", (167, 255, 120), 25, Vector2(340, 50))
        
    ScreenOptions.render_text_on_screen(screen, "Left click to shoot & 'J' to reload (10 bullets = 500$)", (167, 50, 120), 20, Vector2(270, 560))
    ScreenOptions.render_text_on_screen(screen, "'U' to upgrade spaceship speed (1000$)", (167, 250, 120), 20, Vector2(300, 580))




# Objects rendering function
def render_objects():
    enemy_spawner()
    resolve_bullets_movement()
    resolve_enemies_movement()
    display_player_on_screen()
    display_ammo_on_screen()
    display_money_on_screen()
    help_message()




def main():
    global score
    global highscore

    # Get highest score
    with open('data/high-score.txt', 'r') as f:
        line = f.readline()
        highscore = line

    # Game loop
    while game.running:
        # Place background
        screen.fill((0, 0, 0))

        # Handle window events
        game.handle_events()

        # Render objects
        render_objects()

        # Update objects rendered on screen
        pygame.display.update()

    if score >= int(highscore):
        with open('data/high-score.txt', 'w') as f:
            f.write(str(score))


main()





