from scripts.gameengine import *
from scripts.gun import *


class PlayerControls():
    def __init__(self, player_object):
        self.player_object = player_object

    
    def move(self, force: Vector2, speed: float):
        self.player_object.transform.position.x = self.player_object.transform.position.x + (force.x * speed)
        self.player_object.transform.position.y = self.player_object.transform.position.y + (force.x * speed)

    
    def move_horizontally(self, force, speed):
        self.player_object.transform.position.x = self.player_object.transform.position.x + (force * speed)

    
    def move_vertically(self, force, speed):
        self.player_object.transform.position.y = self.player_object.transform.position.y + (force * speed)




class Player:
    def __init__(self):
        self.transform = Transform()
        self.moving_force = Vector2(0, 0)
        self.moving_speed = Vector2(0, 0)
        self.gun = Gun(self)
        self.money = 0


    def set_position(self, position: Vector2):  # position must be a Vector2 object
        self.transform.position.x = position.x
        self.transform.position.y = position.y
        self.controls = PlayerControls(self)

    
    def setup_moving(self, moving_force: Vector2, moving_speed: Vector2):
        self.moving_force = Vector2(moving_force.x, moving_force.y)
        self.moving_speed = Vector2(moving_speed.x, moving_speed.y)

    
    def upgrade_moving_speed(self):
        self.moving_force.x += 1