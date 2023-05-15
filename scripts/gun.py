from scripts.gameengine import Vector2



class Bullet:
    def __init__(self, pos: Vector2):
        self.position = Vector2(pos.x + 35, pos.y)
        self.move_force = 0.5
        self.move_speed = 2


    def move(self):
        self.position.y -= self.move_force * self.move_speed



class Gun:
    def __init__(self, player):
        self.ammo = 5
        self.damage = 5.00
        self.player = player
        self.bullets_shot = []


    def add_ammo(self, amount: int):
        self.ammo += amount

    
    def increase_damage(self, amount: float):
        self.damage += amount

    
    def fire(self):
        fired_bullet = Bullet(self.player.transform.position)
        self.bullets_shot.append(fired_bullet)
        self.ammo -= 1

