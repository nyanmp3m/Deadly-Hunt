import arcade
import enum

class FaceDirection(enum.Enum):
    LEFT = 0
    RIGHT = 1


class Skeleton1(arcade.Sprite):
    def __init__(self):
        super().__init__("Pictures/skeleton/sceleton_attack0.png", scale=0.4)

        self.attack_frames = []
        for i in range(10):
            texture = arcade.load_texture(f"Pictures/skeleton/sceleton_attack{i}.png")
            self.attack_frames.append(texture)

        self.is_attacking = False
        self.current_frame = 0
        self.frame_timer = 0

    def attack_once(self):
        if not self.is_attacking:
            self.is_attacking = True
            self.current_frame = 0
            self.frame_timer = 0

    def update_animation(self, delta_time):
        if self.is_attacking:
            self.frame_timer += delta_time

            if self.frame_timer >= 0.1:
                self.frame_timer = 0
                self.current_frame += 1

                if self.current_frame >= len(self.attack_frames):
                    self.is_attacking = False
                    self.current_frame = 0
                    self.texture = self.attack_frames[0]
                else:
                    self.texture = self.attack_frames[self.current_frame]