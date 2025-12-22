import arcade
import random

from Sprites_classes.SettingsSprite_class import SettingsSprite
from Sprites_classes.SettingsSpriteWindow_class import SettingsWindow
from Sprites_classes.StartGameButtonSprite_class import StartGameButtonSprite
from Sprites_classes.explosion import Explosion
from Sprites_classes.Cursor_texture import Cursor

width_user, height_user = arcade.get_display_size()
images = ["background1.jpg", "background2.jpg"]
background = random.choice(images)


class DeadlyHunt(arcade.View):
    def __init__(self, window):
        super().__init__()
        self.background = arcade.load_texture(f"images/{background}")
        self.window.set_mouse_visible(False)
        self.settings_sprite_list = arcade.SpriteList()
        self.start_game_list = arcade.SpriteList()
        self.explosion_animation_list = arcade.SpriteList()
        self.cursor_list = arcade.SpriteList()

        self.explosion_flag = False

        self.cursor = Cursor(width_user // 2, height_user // 2)
        self.cursor_list.append(self.cursor)

        start_game_button = StartGameButtonSprite()
        self.start_game_list.append(start_game_button)

        setting = SettingsSprite()
        self.settings_sprite_list.append(setting)

        self.fullscreen_flag = True
        self.window = window

        self.flag_mouse_on_start_button = False

    def setup(self):
        pass


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.settings_sprite_list.draw()
        self.start_game_list.draw()
        self.explosion_animation_list.draw()
        self.cursor_list.draw()

    def on_update(self, delta_time):
        finished_animation = []
        for i in self.explosion_animation_list:
            i.update_animation(delta_time)
            if i.finished:
                finished_animation.append(i)

        for i in finished_animation:
            self.explosion_animation_list.remove(i)

        if self.flag_mouse_on_start_button:
            if self.start_game_list[0].center_x < 200:
                self.start_game_list[0].center_x += 5
        else:
            if self.start_game_list[0].center_x > (width_user // 2) - (width_user // 2.5):
                self.start_game_list[0].center_x -= 5

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor_list[0].center_x = x
        self.cursor_list[0].center_y = y

        if len(arcade.get_sprites_at_point((x, y), self.start_game_list)) == 1:
            self.flag_mouse_on_start_button = True
        else:
            self.flag_mouse_on_start_button = False

    def on_mouse_press(self, x, y, button, modifiers):
        if len(self.explosion_animation_list) == 0:
            explosion = Explosion(x, y + 20)
            self.explosion_animation_list.append(explosion)

        settings_sprite_hits = arcade.get_sprites_at_point((x, y), self.settings_sprite_list)

        for sprite in settings_sprite_hits:
            self.window.show_view(SettingsWindow(self.window, self, self.background))


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
