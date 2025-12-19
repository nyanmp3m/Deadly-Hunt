import arcade
import random
import time

from Sprites_classes.SettingsSprite_class import SettingsSprite
from Sprites_classes.SettingsSpriteWindow_class import SettingsWindow

width_user, height_user = arcade.get_display_size()
images = ["background1.jpg", "background2.jpg"]
background = random.choice(images)


class DeadlyHunt(arcade.View):
    def __init__(self, window):
        super().__init__()
        self.background = arcade.load_texture(f"images/{background}")
        self.settings_sprite_list = arcade.SpriteList()

        setting = SettingsSprite()
        self.settings_sprite_list.append(setting)

        self.fullscreen_flag = True
        self.window = window

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.settings_sprite_list.draw()

    def setup(self):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        settings_sprite_hits = arcade.get_sprites_at_point((x, y), self.settings_sprite_list)

        for sprite in settings_sprite_hits:
            self.window.show_view(SettingsWindow(self.window, self))

    def on_key_press(self, key, modifier):
        if key == arcade.key.RCTRL:
            if self.fullscreen_flag:
                self.window.set_fullscreen(False)
                self.fullscreen_flag = False
            elif not self.fullscreen_flag:
                self.window.set_fullscreen(True)
                self.fullscreen_flag = True


def main():
    window = arcade.Window(width_user, height_user, "Deadly_Hunt")
    window.show_view(DeadlyHunt(window))
    arcade.run()


if __name__ == "__main__":
    main()
