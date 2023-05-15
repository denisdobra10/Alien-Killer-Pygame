import pygame
from scripts.gameengine import Vector2

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Setup window title and icon
pygame.display.set_caption("Alien Killer")
icon = pygame.image.load("assets/logo.png")
pygame.display.set_icon(icon)


# Load assets and info
playerImg = pygame.image.load('assets/player.png')
playerInitPos = Vector2(400, 450)

ammoImg = pygame.image.load('assets/bullet.png')
bulletImg = pygame.image.load('assets/bullet.png')
AMMO_IMG_POS = Vector2(700, 35)
AMMO_TEXT_POS = Vector2(740, 45)
ammoImg = pygame.transform.scale(ammoImg, (40, 40))
bulletImg = pygame.transform.scale(bulletImg, (25, 25))

dollarImg = pygame.image.load('assets/dollar.png')
DOLLAR_IMG_POS = Vector2(40, 40)
MONEY_TEXT_POS = Vector2(80, 40)
dollarImg = pygame.transform.scale(dollarImg, (25, 25))

alienImg = pygame.image.load('assets/alien.png')
alienImg = pygame.transform.scale(alienImg, (70, 70))
smallerAlienImg = pygame.transform.scale(alienImg, (40, 40))

# SFX
bullet_attack_sfx = pygame.mixer.Sound("sfx/bullet-attack.wav")
no_ammo_sfx = pygame.mixer.Sound("sfx/no-ammo.mp3")
explosion_sfx = pygame.mixer.Sound("sfx/explosion.wav")
reload_sfx = pygame.mixer.Sound("sfx/reload.mp3")
upgrade_sfx = pygame.mixer.Sound("sfx/upgrade.mp3")

