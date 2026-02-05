import arcade
import enum

class FaceDirection(enum.Enum):
    LEFT = 0
    RIGHT = 1


class Skeleton1(arcade.Sprite):
    def __init__(self):
        super().__init__("Pictures/skeleton/sceleton_attack0.png", scale=0.4, flipped_horizontally=True)

        self.attack_animation = []
        for i in range(10):
            texture = arcade.load_texture(f"Pictures/skeleton/sceleton_attack{i}.png")
            self.attack_animation.append(texture)

        self.is_attacking = False
        self.current_texture = 0
        self.texture_change_time = 0
        self.current_texture1 = 0
        self.texture_change_time1 = 0
        self.texture_change_delay = 0.1
        self.hp = 25
        self.kd = 3
        self.lov = 10
        self.dm = 7
    def update_animation(self, delta_time):
        if self.is_attacking:
            self.texture_change_time += delta_time
            if self.texture_change_time >= self.texture_change_delay:
                self.texture_change_time = 0
                self.current_texture += 1

                if self.current_texture >= len(self.attack_animation ):
                    self.current_texture = 0
                    self.is_attacking = False
                    return