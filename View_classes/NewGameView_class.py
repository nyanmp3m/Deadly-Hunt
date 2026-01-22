import arcade

from Sprites_classes.Cursor_texture import Cursor

width_user, height_user = arcade.get_display_size()


class NewGameWindowView(arcade.View):
    def __init__(self, window):
        super().__init__(window)
        self.window = window
        arcade.set_background_color(arcade.color.GRAY)
        self.cursor_list = arcade.SpriteList()

        self.cursor = Cursor(width_user // 2, height_user // 2)
        self.cursor_list.append(self.cursor)

    def on_draw(self):
        self.clear()
        self.cursor_list.draw()
