import arcade
import random

from Sprites_classes.SettingsSprite_class import SettingsSprite
from Sprites_classes.SettingsSpriteWindow_class import SettingsWindow

width_user, height_user = arcade.get_display_size()
images = ["background1.jpg", "background2.jpg"]
background = random.choice(images)


class DeadlyHunt(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True, fullscreen=False)
        self.background = arcade.load_texture(f"images/{background}")
        self.settings_sprite_list = arcade.SpriteList()
        self.fullscreen_flag = True

        self.main_view = None

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.settings_sprite_list.draw()

    def setup(self):
        setting = SettingsSprite()
        self.settings_sprite_list.append(setting)

    def on_mouse_press(self, x, y, button, modifiers):
        settings_sprite_hits = arcade.get_sprites_at_point((x, y), self.settings_sprite_list)

        for sprite in settings_sprite_hits:
            sprite.remove_from_sprite_lists()

    def on_key_press(self, key, modifier):
        if key == arcade.key.RCTRL:
            if self.fullscreen_flag:
                self.set_fullscreen(False)
                self.fullscreen_flag = False
            elif not self.fullscreen_flag:
                self.set_fullscreen(True)
                self.fullscreen_flag = True


def main():
    game = DeadlyHunt(width_user, height_user, "Deadly_Hunt")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
