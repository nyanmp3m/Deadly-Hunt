import arcade
import random

from Sprites_classes.SettingsSprite_class import SettingsSprite
from View_classes.SettingsSpriteWindow_class import SettingsWindow
from Sprites_classes.StartGameButtonSprite_class import StartGameButtonSprite
from Sprites_classes.ExplosionSprite_class import Explosion
from Sprites_classes.SkeletonSprite_class import Skeleton
from Sprites_classes.GhostSprite_class import GHOST

from independentVariables.variables import Cursor_obj

from View_classes.NewGameView_class import NewGameWindowView

width_user, height_user = arcade.get_display_size()
images = ["background1.jpg", "background2.jpg"]
background = random.choice(images)


class MainMenu(arcade.View):
    def __init__(self, window):
        super().__init__()
        self.background = arcade.load_texture(f"images/{background}")
        self.window.set_mouse_visible(False)
        self.settings_sprite_list = arcade.SpriteList()
        self.start_game_list = arcade.SpriteList()
        self.explosion_animation_list = arcade.SpriteList()
        self.cursor_list = arcade.SpriteList()
        self.skeleton_list = arcade.SpriteList()
        self.ghost_list = arcade.SpriteList()
        self.window = window

        self.explosion_flag = False

        self.cursor = Cursor_obj
        self.cursor_list.append(self.cursor)

        self.start_game_button = StartGameButtonSprite()
        self.start_game_list.append(self.start_game_button)

        setting = SettingsSprite()
        self.settings_sprite_list.append(setting)

        skeleton = Skeleton()
        self.skeleton_list.append(skeleton)

        ghost = GHOST()
        self.ghost_list.append(ghost)

        self.fullscreen_flag = True
        self.window = window

        self.flag_mouse_on_start_button = False

        self.music = arcade.load_sound("Soundtracks/Main_Menu_theme.mp3")
        self.music.play(loop=True, volume=0.5)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.settings_sprite_list.draw()
        self.start_game_list.draw()
        if background == "background1.jpg":
            self.skeleton_list.draw()
        if background == "background2.jpg":
            self.ghost_list.draw()
        self.explosion_animation_list.draw()
        self.cursor_list.draw()

    def on_update(self, delta_time):
        if background == "background1.jpg":
            self.skeleton_list.update()
            for i in self.skeleton_list:
                i.update_animation(delta_time)

        if background == "background2.jpg":
            self.ghost_list.update()
            for i in self.ghost_list:
                i.update_animation(delta_time)

        finished_animation = []
        for i in self.explosion_animation_list:
            i.update_animation(delta_time)
            if i.finished:
                finished_animation.append(i)

        for i in finished_animation:
            self.explosion_animation_list.remove(i)

        if self.flag_mouse_on_start_button:
            if self.start_game_list[0].center_x < ((width_user // 2) - (width_user // 2.5)) + 50:
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
        settings_sprite_hits = arcade.get_sprites_at_point((x, y), self.settings_sprite_list)

        for sprite in settings_sprite_hits:
            self.window.show_view(SettingsWindow(self.window, self, self.background))

        skeleton_hits = arcade.get_sprites_at_point((x, y), self.skeleton_list)

        for sprite in skeleton_hits:
            if not sprite.is_died and sprite.cooldown >= 0.5:
                sprite.is_damaged = True
                sprite.hp -= 1

        ghost_hits = arcade.get_sprites_at_point((x, y), self.ghost_list)
        for sprite in ghost_hits:
            if not sprite.disappeared and not sprite.disappearing and not sprite.invisible and sprite.cooldown >= 0.5:
                sprite.disappearing = True

        start_game_button_hits = arcade.get_sprites_at_point((x, y), self.start_game_list)
        if self.start_game_button.collides_with_point((x, y)):
            new_game_menu = NewGameWindowView(self.window, self)
            self.window.show_view(new_game_menu)

        if len(self.explosion_animation_list) == 0 and len(settings_sprite_hits) == 0 and len(start_game_button_hits) == 0:
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


def main():
    window = arcade.Window(width_user, height_user, "Deadly_Hunt")
    window.show_view(MainMenu(window))
    arcade.run()


if __name__ == "__main__":
    main()
