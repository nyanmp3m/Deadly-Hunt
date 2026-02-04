import arcade

from Sprites_classes.ExplosionSprite_class import Explosion

from independentVariables.variables import Cursor_obj

from Sprites_classes.StartMainGameButtonSprite_class import StartMainGameButtonSprite
from View_classes.ExplanatoryNoteWindow_class import ExplanatoryNote

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
        self.white_player = arcade.Sprite("TrainingLevel/Testing_hero/Egor(White_Hero).png")
        self.white_player_list.append(self.white_player)

        self.black_player_list = arcade.SpriteList()
        self.black_player = arcade.Sprite("TrainingLevel/Testing_hero/Black_hero.png")
        self.black_player_list.append(self.black_player)

        self.left_arrow_list = arcade.SpriteList()
        self.left_arrow = arcade.Sprite("TrainingLevel/Testing_hero/Left_arrow.png")
        self.left_arrow_list.append(self.left_arrow)

        self.right_arrow_list = arcade.SpriteList()
        self.right_arrow = arcade.Sprite("TrainingLevel/Testing_hero/Right_arrow.png")
        self.right_arrow_list.append(self.right_arrow)


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture, arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.start_game_button_list.draw()
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
