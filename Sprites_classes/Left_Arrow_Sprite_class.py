import arcade

width_user, height_user = arcade.get_display_size()

class Left_Arrow_Sprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.3

        self.texture = arcade.load_texture("TrainingLevel/Testing_hero/Left_arrow.png")
        self.center_x = width_user * 0.3
        self.center_y = height_user * 0.5