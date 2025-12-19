import arcade

from StartingWindow.StartingWindow import width_user, height_user


class StartGameButtonSprite(arcade.Sprite):
    def __init__(self):
        super.__init__()

        self.texture = arcade.load_texture("StartGameButton.png")
        self.center_x = width_user / 2
        self.center_y = height_user / 2

