import arcade
import enum
import random
from arcade.examples.gl.game_of_life_colors import CELL_SIZE
from arcade.particles import FadeParticle, Emitter, EmitBurst

width_user, height_user = arcade.get_display_size()


class FaceDirection(enum.Enum):
    LEFT = 0
    RIGHT = 1

class GHOST(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.flying_animation = []
        self.disappearing_animation = []
        self.appearing_animation = []
        for i in range(1, 9):
            texture = arcade.load_texture(f"Pictures/Ghost/ghost{i}.png")
            self.flying_animation.append(texture)
        for i in range(1, 19):
            texture1 = arcade.load_texture(f"Pictures/Ghost/ghost_a{i}.png")
            self.disappearing_animation.append(texture1)

        self.appearing_animation = self.disappearing_animation[::-1]

        self.center_x = width_user / 2
        self.center_y = height_user / 2
        self.speed_x = random.choice(range(35, 61))
        self.speed_y = random.choice(range(35, 61))
        self.face_direction = FaceDirection.RIGHT
        self.current_texture = 0
        self.texture_change_time = 0
        self.current_texture1 = 0
        self.texture_change_time1 = 0
        self.current_texture3 = 0
        self.texture_change_time3 = 0
        self.texture_change_delay = 0.1
        self.scale = 2
        self.disappeared = False
        self.disappearing = False
        self.appearing = False
        self.invisible = 0.0
        self.cooldown = 0.0


    def update(self, delta_time):
        if not self.disappearing and not self.appearing:
            self.center_x += self.speed_x * delta_time
            self.center_y += self.speed_y * delta_time
            if self.left < CELL_SIZE:
                self.speed_x = random.choice(range(35, 61))
                self.speed_y = random.choice(range(35, 61))
                self.speed_x = self.speed_x
                self.speed_y = self.speed_y
                self.face_direction = FaceDirection.RIGHT
            if self.right > width_user - CELL_SIZE:
                self.speed_x = random.choice(range(35, 61))
                self.speed_y = random.choice(range(35, 61))
                self.speed_x = -self.speed_x
                self.speed_y = -self.speed_y
                self.face_direction = FaceDirection.LEFT
            if self.top > height_user - CELL_SIZE:
                self.speed_x = random.choice(range(35, 61))
                self.speed_y = random.choice(range(35, 61))
                self.speed_x = self.speed_x
                self.speed_y = -self.speed_y
                self.face_direction = FaceDirection.RIGHT
            if self.bottom < CELL_SIZE:
                self.speed_x = random.choice(range(35, 61))
                self.speed_y = random.choice(range(35, 61))
                self.speed_x = -self.speed_x
                self.speed_y = self.speed_y
                self.face_direction = FaceDirection.LEFT


    def update_animation(self, delta_time: float = 1 / 60):

        if self.disappearing:
            self.texture_change_time1 += delta_time
            if self.texture_change_time1 >= self.texture_change_delay:
                self.texture_change_time1 = 0
                self.current_texture1 += 1

                if self.current_texture1 >= len(self.disappearing_animation):
                    self.disappeared = True
                    self.disappearing = False
                    return

                if self.face_direction == FaceDirection.RIGHT:
                    self.texture = self.disappearing_animation[self.current_texture1]
                else:
                    self.texture = self.disappearing_animation[self.current_texture1].flip_horizontally()

        if not self.disappearing and not self.appearing:
            self.cooldown += delta_time

            if self.disappeared and self.invisible < 15:
                self.alpha = 0
                self.invisible += delta_time

            if self.invisible >= 15:
                self.alpha = 255
                self.invisible = 0.0
                self.disappearing = False
                self.disappeared = False
                self.appearing = True


            self.texture_change_time += delta_time
            if self.texture_change_time >= self.texture_change_delay:
                self.texture_change_time = 0
                self.current_texture += 1

                if self.current_texture >= len(self.flying_animation):
                    self.current_texture = 0

                if self.face_direction == FaceDirection.RIGHT:
                    self.texture = self.flying_animation[self.current_texture]
                else:
                    self.texture = self.flying_animation[self.current_texture].flip_horizontally()

        if self.appearing and not self.disappearing:
            self.cooldown = 0.0
            self.texture_change_time3 += delta_time
            if self.texture_change_time3 >= self.texture_change_delay:
                self.texture_change_time3 = 0
                self.current_texture3 += 1

                if self.current_texture3 >= len(self.appearing_animation):
                    self.current_texture = 0
                    self.texture_change_time = 0
                    self.current_texture1 = 0
                    self.texture_change_time1 = 0
                    self.current_texture3 = 0
                    self.texture_change_time3 = 0
                    self.appearing = False
                    self.invisible = 0.0
                    return

                if self.face_direction == FaceDirection.RIGHT:
                    self.texture = self.appearing_animation[self.current_texture3]
                else:
                    self.texture = self.appearing_animation[self.current_texture3].flip_horizontally()
