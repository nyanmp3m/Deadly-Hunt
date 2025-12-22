import arcade


class Explosion(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__()
        self.explosion_animation = []
        for i in range(1, 5):
            texture = arcade.load_texture(f'Pictures/Explosion{i}.png')
            self.explosion_animation.append(texture)

        self.current_texture = 0
        self.texture_change_time = 0
        self.texture_change_delay = 0.1
        self.finished = False
        self.scale = 0.7

        self.center_x = center_x
        self.center_y = center_y
        self.texture = self.explosion_animation[0]

    def update_animation(self, delta_time: float = 1 / 60):
        if not self.finished:
            self.texture_change_time += delta_time

            if self.texture_change_time >= self.texture_change_delay:
                self.texture_change_time = 0
                self.current_texture += 1

                if self.current_texture >= len(self.explosion_animation):
                    self.finished = True
                    return

                self.texture = self.explosion_animation[self.current_texture]