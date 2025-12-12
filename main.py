from pyglet.event import EVENT_HANDLE_STATE

from Sprites_classes.SettingsSprite_class import SettingsSprite
import arcade

width_user, height_user = arcade.get_display_size()


class MainWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False, fullscreen=False)
        self.background_color = arcade.color.TEA_GREEN
        self.sprite_list = arcade.SpriteList()

    def setup(self):
        pass

    def on_draw(self):
        setting = SettingsSprite()
        self.sprite_list.append(setting)

        self.clear()
        self.sprite_list.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        setting_hit = arcade.get_sprites_at_point((x, y), self.sprite_list)



def main():
    game = MainWindow(width_user, height_user, "Deadly_Hunt")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
