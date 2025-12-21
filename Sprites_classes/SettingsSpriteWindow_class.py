from Sprites_classes.Cursor_texture import Cursor
from Sprites_classes.explosion import Explosion

import arcade
import random

width_user, height_user = arcade.get_display_size()

class SettingsWindow(arcade.View):
    def __init__(self, window, main_view, background):
        super().__init__()
        self.window = window
        self.is_activate = False

        self.background = background

        self.cursor_list = arcade.SpriteList()
        self.cursor = Cursor(width_user // 2, height_user // 2)
        self.cursor_list.append(self.cursor)

        self.explosion_list = arcade.SpriteList()

        self.main_view = main_view

    def on_draw(self):
        self.clear()

        arcade.draw_texture_rect(self.background,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))

        texture = arcade.load_texture("Pictures/SettingsSpriteWindow_picture.png")
        arcade.draw_texture_rect(texture, arcade.rect.XYWH(500, 500, 550, 900))

        self.explosion_list.draw()
        self.cursor_list.draw()

    def on_key_press(self, key, modifier):
        if key == arcade.key.ESCAPE:
            self.window.show_view(self.main_view)

    def on_update(self, delta_time):
        finished_animation = []
        for i in self.explosion_list:
            i.update_animation(delta_time)
            if i.finished:
                finished_animation.append(i)

        for i in finished_animation:
            self.explosion_list.remove(i)

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.cursor_list[0].center_x = x
        self.cursor_list[0].center_y = y

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        explosion = Explosion(x, y + 20)
        self.explosion_list.append(explosion)