import arcade

width_user, height_user = arcade.get_display_size()


class Right_Arrow_Sprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.3

        self.texture = arcade.load_texture("TrainingLevel/Testing_hero/Right_arrow.png")
        self.center_x = width_user * 0.7
        self.center_y = height_user * 0.5