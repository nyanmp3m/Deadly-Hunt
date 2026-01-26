import arcade

from Sprites_classes.Cursor_texture import Cursor

width_user, height_user = arcade.get_display_size()

Cursor_obj = Cursor(width_user // 2, height_user // 2)