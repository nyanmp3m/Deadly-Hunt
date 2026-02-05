import arcade
import enum

PLAYER_SPEED = 2.5

class FaceDirection(enum.Enum):
    LEFT = 0
    RIGHT = 1


class EgorB(arcade.Sprite):
    def __init__(self):
        super().__init__(
            "TrainingLevel/EgorB.png",
            scale=0.18
        )
        self.jump_count = 0
        self.is_walking = False
        self.is_jumping = False
        self.walking_animation = []
        self.jumping_animation = []
        self.current_texture = 0
        self.texture_change_time = 0
        self.current_texture1 = 0
        self.texture_change_time1 = 0
        self.texture_change_delay = 0.1
        self.face_direction = FaceDirection.RIGHT

        for i in range(1, 6):
            texture = arcade.load_texture(f"TrainingLevel/walkingB{i}.png")
            self.walking_animation.append(texture)
        for i in range(1, 4):
            texture = arcade.load_texture(f"TrainingLevel/jumpB{i}.png")
            self.jumping_animation.append(texture)

    def update(self, delta_time):
        super().update()

    def update_animation(self, delta_time: float = 1/5):
        if self.is_walking:
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
        if self.is_jumping:
            self.texture_change_time1 += delta_time
            if self.texture_change_time1 >= self.texture_change_delay:
                self.texture_change_time1 = 0
                self.current_texture1 += 1

                if self.current_texture1 >= len(self.jumping_animation):
                    self.current_texture1 = 0

                if self.face_direction == FaceDirection.RIGHT:
                    self.texture = self.jumping_animation[self.current_texture1]
                else:
                    self.texture = self.jumping_animation[self.current_texture1].flip_horizontally()



    def jump(self):
        if self.jump_count < 1:
            self.change_y = PLAYER_SPEED * 3.5
            self.is_jumping = True
            self.jump_count += 1

    def move_left(self):
        self.change_x = -PLAYER_SPEED
        self.is_walking = True
        self.face_direction = FaceDirection.RIGHT

    def move_right(self):
        self.change_x = PLAYER_SPEED
        self.is_walking = True
        self.face_direction = FaceDirection.LEFT

    def stop_horizontal(self):
        self.change_x = 0
        self.is_walking = False
        self.current_texture = 0
        if self.face_direction == FaceDirection.RIGHT:
            self.texture = self.walking_animation[self.current_texture]
        else:
            self.texture = self.walking_animation[self.current_texture].flip_horizontally()

    def stop_vertical(self):
        self.change_y = 0
        self.is_jumping = False
        if self.face_direction == FaceDirection.RIGHT:
            self.texture = self.walking_animation[self.current_texture]
        else:
            self.texture = self.walking_animation[self.current_texture].flip_horizontally()
