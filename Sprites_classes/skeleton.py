import arcade
import enum
from arcade.examples.gl.game_of_life_colors import CELL_SIZE
width_user, height_user = arcade.get_display_size()

class FaceDirection(enum.Enum):
    LEFT = 0
    RIGHT = 1

class Skeleton(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.walking_animation = []
        self.damaged_animation = []
        self.died_animation = []
        for i in range(1, 11):
            texture = arcade.load_texture(f"Pictures/skeleton/skeleton_walk{i}.png")
            self.walking_animation.append(texture)

        for i in range(1, 6):
            texture1 = arcade.load_texture(f"Pictures/skeleton/damaged_{i}.png")
            self.damaged_animation.append(texture1)

        for i in range(0, 10):
            texture2 = arcade.load_texture(f"Pictures/skeleton/died ({i}).png")
            self.died_animation.append(texture2)

        self.reborn_animation = self.died_animation[::-1]

        self.hp = 5
        self.reborn = 0.0
        self.cooldown = 0.0
        self.current_texture3 = 0
        self.texture_change_time3 = 0
        self.current_texture2 = 0
        self.texture_change_time2 = 0
        self.current_texture = 0
        self.texture_change_time = 0
        self.current_texture1 = 0
        self.texture_change_time1 = 0
        self.is_damaged = False
        self.is_died = False
        self.texture_change_delay = 0.1
        self.texture_change_delay1 = 0.1
        self.center_y = 130
        self.center_x = width_user / 2
        self.scale = 3
        self.CELL_SIZE = 100
        self.speed = 50
        self.face_direction = FaceDirection.RIGHT


    def update(self, delta_time):
        if self.is_damaged:
            self.cooldown = 0.0
        if not self.is_damaged and self.hp > 0:
            self.cooldown += delta_time
            if self.speed > 0:
                self.face_direction = FaceDirection.RIGHT
            self.center_x += self.speed * delta_time
            if self.left < CELL_SIZE or self.right > width_user - CELL_SIZE:
                self.speed = -self.speed
                self.face_direction = FaceDirection.LEFT
        if self.hp == 0:
            self.reborn += delta_time

    def update_animation(self, delta_time: float = 1 / 60):
        if self.hp == 0 and self.reborn < 10.0:
            self.texture_change_time2 += delta_time
            if self.texture_change_time2 >= self.texture_change_delay:
                self.texture_change_time2 = 0
                self.current_texture2 += 1

                if self.current_texture2 >= len(self.died_animation):
                    self.is_died = True
                    return

                if self.face_direction == FaceDirection.RIGHT:
                    self.texture = self.died_animation[self.current_texture2]
                else:
                    self.texture = self.died_animation[self.current_texture2].flip_horizontally()

        if self.hp == 0 and self.reborn >= 10.0:
            self.texture_change_time3 += delta_time
            if self.texture_change_time3 >= self.texture_change_delay:
                self.texture_change_time3 = 0
                self.current_texture3 += 1

                if self.current_texture3 >= len(self.reborn_animation):
                    self.hp = 5
                    self.reborn = 0.0
                    self.current_texture3 = 0
                    self.texture_change_time3 = 0
                    self.current_texture2 = 0
                    self.texture_change_time2 = 0
                    self.current_texture = 0
                    self.texture_change_time = 0
                    self.current_texture1 = 0
                    self.texture_change_time1 = 0
                    self.is_damaged = False
                    self.is_died = False
                    return

                if self.face_direction == FaceDirection.RIGHT:
                    self.texture = self.reborn_animation[self.current_texture3]
                else:
                    self.texture = self.reborn_animation[self.current_texture3].flip_horizontally()

        elif self.is_damaged and self.hp > 0:
            self.texture_change_time1 += delta_time

            if self.texture_change_time1 >= self.texture_change_delay1:
                self.texture_change_time1 = 0
                self.current_texture1 += 1

                if self.current_texture1 >= len(self.damaged_animation):
                    self.is_damaged = False
                    self.current_texture1 = 0

                if self.face_direction == FaceDirection.RIGHT:
                    self.texture = self.damaged_animation[self.current_texture1]

                else:
                    self.texture = self.damaged_animation[self.current_texture1].flip_horizontally()

        elif self.hp > 0 and not self.is_damaged:
            self.texture_change_time += delta_time
            if self.texture_change_time >= self.texture_change_delay:
                self.texture_change_time = 0
                self.current_texture += 1

                if self.current_texture >= len(self.walking_animation):
                    self.current_texture = 0

                if self.face_direction == FaceDirection.RIGHT:
                    self.texture = self.walking_animation[self.current_texture]
                else:
                    self.texture = self.walking_animation[self.current_texture].flip_horizontally()


