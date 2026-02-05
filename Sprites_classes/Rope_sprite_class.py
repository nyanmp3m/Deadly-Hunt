import arcade

width_user, height_user = arcade.get_display_size()


class Rope(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.25

        self.texture = arcade.load_texture("TrainingLevel/rope_attack.png")
        self.center_x = width_user * 0.45
        self.center_y = height_user * 0.15