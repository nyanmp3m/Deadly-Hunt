import arcade

width_user, height_user = arcade.get_display_size()

class StartGameButtonSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.8

        self.texture = arcade.load_texture("Pictures/StartGameButton_picture.png")
        self.center_x = (width_user // 2) - (width_user // 2.5)
        self.center_y = height_user // 2


