import arcade

width_user, height_user = arcade.get_display_size()

class SettingsWindow(arcade.View):
    def on_show_view(self):
        print("Show")

    def on_draw(self):
        texture = arcade.load_texture("Pictures/SettingsSpriteWindow_picture.png")
        arcade.draw_texture_rect(texture, arcade.rect.XYWH(500, 500, 300, 600))
