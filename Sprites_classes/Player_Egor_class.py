import arcade

PLAYER_SPEED = 2.5


class Egor(arcade.Sprite):
    def __init__(self):
        super().__init__(
            "TrainingLevel/Egor(White_Hero).png",
            scale=0.1
        )
        self.jump_count = 0

    def update(self, delta_time):
        super().update()

    def jump(self):
        if self.jump_count < 1:
            self.change_y = PLAYER_SPEED * 3.5
            self.jump_count += 1

    def move_left(self):
        self.change_x = -PLAYER_SPEED

    def move_right(self):
        self.change_x = PLAYER_SPEED

    def stop_horizontal(self):
        self.change_x = 0

    def stop_vertical(self):
        self.change_y = 0