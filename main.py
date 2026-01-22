import arcade

from Sprites_classes.SettingsSprite_class import SettingsSprite

width_user, height_user = arcade.get_display_size()


class MainWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False, fullscreen=False)
        self.background_color = arcade.color.TEA_GREEN
        self.settings_sprite_list = arcade.SpriteList()

    def setup(self):
        setting = SettingsSprite()
        self.settings_sprite_list.append(setting)

    def on_draw(self):
        self.clear()
        self.settings_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        settings_sprite_hits = arcade.get_sprites_at_point((x, y), self.settings_sprite_list)

        for sprite in settings_sprite_hits:
            sprite.remove_from_sprite_lists()


def main():
    game = MainWindow(width_user, height_user, "Deadly_Hunt")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
