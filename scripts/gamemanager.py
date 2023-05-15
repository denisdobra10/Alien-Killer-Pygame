from scripts.player import *
from scripts.eventshandler import *
from scripts.enemy import EnemySpawner





class Game:
    def __init__(self, player: Player):
        self.running = True
        self.player = player
        self.enemies = []
        self.enemy_spawner = EnemySpawner(self.enemies)


    def handle_events(self):
        check_events(self)
    

