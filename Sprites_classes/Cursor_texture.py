import arcade

width_user, height_user = arcade.get_display_size()


class Cursor(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.cursor_x = x
        self.cursor_y = y
        texture = arcade.load_texture("Pictures/cursor_texture.png")
        self.texture = texture
        self.scale = 0.1
