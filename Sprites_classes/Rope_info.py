import arcade

width_user, height_user = arcade.get_display_size()

class RopeI(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 2
        self.texture = arcade.load_texture("TrainingLevel/rope_i.png")
        self.center_x = width_user * 0.5
        self.center_y = height_user * 0.2