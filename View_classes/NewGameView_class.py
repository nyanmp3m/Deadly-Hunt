import arcade

from Sprites_classes.Cursor_texture import Cursor
from Sprites_classes.ExplosionSprite_class import Explosion

width_user, height_user = arcade.get_display_size()


class NewGameWindowView(arcade.View):
    def __init__(self, window, Cursor):
        super().__init__(window)
        self.window = window
        self.texture = arcade.load_texture("Pictures/New_game_menu_background.png")
        self.cursor_list = arcade.SpriteList()

        self.cursor = Cursor
        self.cursor_list.append(self.cursor)

        self.explosion_flag = False
        self.explosion_animation_list = arcade.SpriteList()

        self.heads_list = arcade.SpriteList()

        self.fullscreen_flag = True

        # Текущий индекс выбранной головы
        self.current_head_index = 0

        # Загружаем все головы, но будем показывать только одну
        self.white_head = arcade.Sprite("Pictures/Characters/White_head_for_sprite.png", scale=0.5)
        self.white_head.center_x = width_user * 0.3
        self.white_head.center_y = height_user * 0.7
        self.heads_list.append(self.white_head)

        self.brown_head = arcade.Sprite("Pictures/Characters/Brown_head_for_sprite.png", scale=0.5)
        self.brown_head.center_x = width_user * 0.3
        self.brown_head.center_y = height_user * 0.7
        self.brown_head.visible = False
        self.heads_list.append(self.brown_head)

        self.yellow_head = arcade.Sprite("Pictures/Characters/Yellow_head_for_sprite.png", scale=0.5)
        self.yellow_head.center_x = width_user * 0.3
        self.yellow_head.center_y = height_user * 0.7
        self.yellow_head.visible = False
        self.heads_list.append(self.yellow_head)


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.texture, arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.heads_list.draw()
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

    def on_key_press(self, key, modifier):
        if key == arcade.key.RCTRL:
            if self.fullscreen_flag:
                self.window.set_fullscreen(False)
                self.fullscreen_flag = False
            elif not self.fullscreen_flag:
                self.window.set_fullscreen(True)
                self.fullscreen_flag = True
