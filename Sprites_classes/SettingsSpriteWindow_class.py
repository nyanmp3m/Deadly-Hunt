import arcade

width_user, height_user = arcade.get_display_size()

class SettingsWindow(arcade.View):
    def __init__(self, window, main_view):
        super().__init__()
        self.window = window
        self.is_activate = False

        self.main_view = main_view

    def on_draw(self):
        texture = arcade.load_texture("Pictures/SettingsSpriteWindow_picture.png")
        arcade.draw_texture_rect(texture, arcade.rect.XYWH(500, 500, 550, 900))

    def on_key_press(self, key, modifier):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.main_view)