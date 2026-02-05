import arcade

from Sprites_classes.ExplosionSprite_class import Explosion

from independentVariables.variables import Cursor_obj

from Sprites_classes.StartMainGameButtonSprite_class import StartMainGameButtonSprite
from View_classes.ExplanatoryNoteWindow_class import ExplanatoryNote

from Sprites_classes.White_Hero_Sprite_class import White_Hero_Sprite
from Sprites_classes.Black_Hero_Sprite_class import Black_Hero_Sprite

from Sprites_classes.Left_Arrow_Sprite_class import Left_Arrow_Sprite
from Sprites_classes.Right_Arrow_Sprite_class import Right_Arrow_Sprite

from Sprites_classes.Save_Hero_Button_Sprite_class import Save_Hero_Button_Sprite
import View_classes.buffer as buffer_module


width_user, height_user = arcade.get_display_size()


class NewGameWindowView(arcade.View):
    def __init__(self, window,starting_window):
        super().__init__(window)
        self.window = window
        self.texture = arcade.load_texture("Pictures/New_game_menu_background.png")
        self.cursor_list = arcade.SpriteList()
        self.start_game_button_list = arcade.SpriteList()

        self.cursor = Cursor_obj
        self.cursor_list.append(self.cursor)

        self.start_game_button = StartMainGameButtonSprite()
        self.start_game_button_list.append(self.start_game_button)

        self.starting_window_view = starting_window

        self.explosion_flag = False
        self.explosion_animation_list = arcade.SpriteList()

        self.fullscreen_flag = True

        self.white_player_list = arcade.SpriteList()
        self.white_player = White_Hero_Sprite()
        self.white_player_list.append(self.white_player)
        self.white_player.visible = True

        self.black_player_list = arcade.SpriteList()
        self.black_player = Black_Hero_Sprite()
        self.black_player_list.append(self.black_player)
        self.black_player.visible = False

        self.left_arrow_list = arcade.SpriteList()
        self.left_arrow = Left_Arrow_Sprite()
        self.left_arrow_list.append(self.left_arrow)

        self.right_arrow_list = arcade.SpriteList()
        self.right_arrow = Right_Arrow_Sprite()
        self.right_arrow_list.append(self.right_arrow)

        self.save_hero_button_list = arcade.SpriteList()
        self.save_hero_button = Save_Hero_Button_Sprite()
        self.save_hero_button_list.append(self.save_hero_button)

        self.current_index = 0


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture, arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.start_game_button_list.draw()
        self.white_player_list.draw()
        self.black_player_list.draw()
        self.left_arrow_list.draw()
        self.right_arrow_list.draw()
        self.save_hero_button_list.draw()
        arcade.draw_text("CHOOSE YOUR CHARACTER", width_user*0.5, height_user*0.8, arcade.color.BLACK, 35, font_name='Times New Roman')
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

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor_list[0].center_x = x
        self.cursor_list[0].center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if len(self.explosion_animation_list) == 0:
            explosion = Explosion(x, y + 20)
            self.explosion_animation_list.append(explosion)
        start_button_hits = arcade.get_sprites_at_point((x, y), self.start_game_button_list)

        if self.left_arrow.collides_with_point((x, y)):
            if self.current_index == 0:
                self.black_player.visible = True
                self.white_player.visible = False
                self.current_index = 1
            elif self.current_index == 1:
                self.black_player.visible = False
                self.white_player.visible = True
                self.current_index = 0

        if self.right_arrow.collides_with_point((x, y)):
            if self.current_index == 0:
                self.black_player.visible = True
                self.white_player.visible = False
                self.current_index = 1
            elif self.current_index == 1:
                self.black_player.visible = False
                self.white_player.visible = True
                self.current_index = 0

        if self.save_hero_button.collides_with_point((x, y)):
            if self.current_index == 0:
                buffer_module.chosen_player = "white"
            elif self.current_index == 1:
                buffer_module.chosen_player = "black"



        for sprite in start_button_hits:
            note = ExplanatoryNote()
            self.window.show_view(note)

    def on_key_press(self, key, modifier):
        if key == arcade.key.RCTRL:
            if self.fullscreen_flag:
                self.window.set_fullscreen(False)
                self.fullscreen_flag = False
            elif not self.fullscreen_flag:
                self.window.set_fullscreen(True)
                self.fullscreen_flag = True

        elif key == arcade.key.ESCAPE:
            self.window.show_view(self.starting_window_view)
