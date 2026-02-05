import arcade

width_user, height_user = arcade.get_display_size()


class Knife(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.3

        self.texture = arcade.load_texture("TrainingLevel/knife_attack.png")
        self.center_x = width_user * 0.35
        self.center_y = height_user * 0.15