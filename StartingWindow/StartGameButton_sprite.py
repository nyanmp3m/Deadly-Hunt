import arcade

width_user, height_user = arcade.get_display_size()

class StartGameButton(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture("")

        self.center_x = width_user // 2
        self.center_y = height_user // 2