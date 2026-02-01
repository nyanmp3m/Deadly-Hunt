import arcade

width_user, height_user = arcade.get_display_size()


class StartMainGameButtonSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.3

        self.texture = arcade.load_texture("Pictures/StartButton.png")
        self.center_x = 200
        self.center_y = 100
