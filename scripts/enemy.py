from scripts.gameengine import Vector2, Transform
import random


class EnemySpawner:
    def __init__(self, enemy_list):
        self.enemies = enemy_list
        self.timer = 5.00

    
    def spawn_enemy(self, big_enemy: bool, startPos=None):
        new_enemy = None
        if startPos is None:
            new_enemy = Enemy(big_enemy, Vector2(random.randint(10, 300), -20))
        else:
            new_enemy = Enemy(big_enemy, startPos)

        new_enemy.setup_moving(Vector2(float(random.randint(1, 5) / 5), float(random.randint(1, 2) / 10)), Vector2(float(random.randint(1, 5)) / random.randint(1, 5), float(random.randint(1, 2)) / random.randint(1, 5)) )
        self.enemies.append(new_enemy)
    





class Enemy:
    def __init__(self, big_enemy: bool, startPos: Vector2):
        self.transform = Transform()
        self.moving_force = Vector2(float(random.randint(1, 5) / 10), float(random.randint(1, 2) / 10))
        self.moving_speed = Vector2(5, 0.5)
        self.money = random.randint(40, 300)
        self.big_enemy = big_enemy

        if big_enemy is True:
            self.money = random.randint(40, 300)
        else:
            self.money = random.randint(25, 175)

        self.direction = "right"
        self.set_position(startPos)


    def set_position(self, position: Vector2):  # position must be a Vector2 object
        self.transform.position.x = position.x
        self.transform.position.y = position.y

    
    def setup_moving(self, moving_force: Vector2, moving_speed: Vector2):
        self.moving_force = moving_force
        self.moving_speed = moving_speed


    def move_horizontally(self, right):
        if right is True:
            self.transform.position.x = self.transform.position.x + (self.moving_force.x * self.moving_speed.x)
        else:
            self.transform.position.x = self.transform.position.x + -(self.moving_force.x * self.moving_speed.x)

    
    def move_vertically(self):
        self.transform.position.y = self.transform.position.y + (self.moving_force.y * self.moving_speed.y)