import arcade
import random

from Sprites_classes.ElfCharacterSprite_class import ElfCharacterSprite
from Sprites_classes.SettingsSprite_class import SettingsSprite
from Sprites_classes.SettingsSpriteWindow_class import SettingsWindow
from Sprites_classes.StartGameButtonSprite_class import StartGameButtonSprite
from Sprites_classes.explosion import Explosion
from Sprites_classes.skeleton import Skeleton
from Sprites_classes.CharacterChangingButtonSprite_class import CharacterChangeButtonSprite
from Sprites_classes.KnightCharacterSprite_class import KnightCharacterSprite
from Sprites_classes.GnomeCharacterSprite_class import GnomeCharacterSprite
from Sprites_classes.SamuraiCharacterSprite_class import SamuraiCharacterSprite
from Sprites_classes.GladiatorCharacterSprite_class import GladiatorCharacterSprite
from Sprites_classes.ElfCharacterSprite_class import ElfCharacterSprite
from Sprites_classes.ChangeCharacterArrowLeftSprite_class import ChangeCharacterArrowLeftSprite
from Sprites_classes.ChangeCharacterArrowRightSprite_class import ChangeCharacterArrowRightSprite
from Sprites_classes.ApproveCharacterButtonSprite_class import ApproveCharacterButtonSprite
from Sprites_classes.Cursor_texture import Cursor


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
        self.change_character_button_list = arcade.SpriteList()
        self.window = window

        self.explosion_flag = False

        self.cursor = Cursor(width_user // 2, height_user // 2)
        self.cursor_list.append(self.cursor)

        self.start_game_button = StartGameButtonSprite()
        self.start_game_list.append(self.start_game_button)

        self.change_character_button = CharacterChangeButtonSprite()
        self.change_character_button_list.append(self.change_character_button)

        setting = SettingsSprite()
        self.settings_sprite_list.append(setting)

        skeleton = Skeleton()
        self.skeleton_list.append(skeleton)

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
        self.change_character_button_list.draw()
        if background == "background1.jpg":
            self.skeleton_list.draw()
        self.explosion_animation_list.draw()
        self.cursor_list.draw()

    def on_update(self, delta_time):
        if background == "background1.jpg":
            self.skeleton_list.update()
            for i in self.skeleton_list:
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
        if len(self.explosion_animation_list) == 0:
            explosion = Explosion(x, y + 20)
            self.explosion_animation_list.append(explosion)

        settings_sprite_hits = arcade.get_sprites_at_point((x, y), self.settings_sprite_list)

        for sprite in settings_sprite_hits:
            self.window.show_view(SettingsWindow(self.window, self, self.background))

        skeleton_hits = arcade.get_sprites_at_point((x, y), self.skeleton_list)

        for sprite in skeleton_hits:
            if not sprite.is_died and sprite.cooldown >= 0.5:
                sprite.is_damaged = True
                sprite.hp -= 1

        if self.start_game_button.collides_with_point((x, y)):
            game_view = GameView(self.window)
            self.window.show_view(game_view)

        if self.change_character_button.collides_with_point((x, y)):
            character_change_view = CharacterChangeView(self.window)
            self.window.show_view(character_change_view)

    def on_key_press(self, key, modifier):
        if key == arcade.key.RCTRL:
            if self.fullscreen_flag:
                self.window.set_fullscreen(False)
                self.fullscreen_flag = False
            elif not self.fullscreen_flag:
                self.window.set_fullscreen(True)
                self.fullscreen_flag = True


class GameView(arcade.View):
    def __init__(self, window):
        super().__init__(window)
        self.background = arcade.color.DARK_GREEN
        self.window = window
        self.fullscreen = False
        arcade.set_background_color(self.background)
        self.window.set_mouse_visible(False)

        self.explosion_animation_list = arcade.SpriteList()
        self.explosion_flag = False

        self.cursor_list = arcade.SpriteList()

        self.cursor = Cursor(width_user // 2, height_user // 2)
        self.cursor_list.append(self.cursor)

        self.flag_mouse_on_start_button = False
        self.fullscreen_flag = True

    def on_draw(self):
        self.clear()
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

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RCTRL:
            if not self.fullscreen:
                self.window.set_fullscreen(False)
                self.fullscreen = True
            elif self.fullscreen:
                self.window.set_fullscreen(True)
                self.fullscreen = False

        if key == arcade.key.ESCAPE:
            main_menu = MainMenu(self.window)
            self.window.show_view(main_menu)





class CharacterChangeView(arcade.View):
    def __init__(self, window):
        super().__init__(window)
        self.background = arcade.color.DARK_GREEN
        self.window = window
        self.fullscreen = False
        self.background = arcade.load_texture("Pictures/Character_changing_menu_background.png")
        self.window.set_mouse_visible(False)
        self.cursor_list = arcade.SpriteList()
        self.explosion_animation_list = arcade.SpriteList()

        self.explosion_flag = False

        self.cursor = Cursor(width_user // 2, height_user // 2)
        self.cursor_list.append(self.cursor)

        self.characters_choice_list = arcade.SpriteList()
        self.current_character_index = 0
        self.characters_names = ["Рыцарь", "Гном", "Самурай", "Гладиатор", "Эльф"]

        self.knight_character = KnightCharacterSprite()
        self.characters_choice_list.append(self.knight_character)
        self.knight_character.visible = True

        self.gnome_character = GnomeCharacterSprite()
        self.characters_choice_list.append(self.gnome_character)
        self.gnome_character.visible = False

        self.samurai_character = SamuraiCharacterSprite()
        self.characters_choice_list.append(self.samurai_character)
        self.samurai_character.visible = False

        self.gladiator_character = GladiatorCharacterSprite()
        self.characters_choice_list.append(self.gladiator_character)
        self.gladiator_character.visible = False

        self.elf_character = ElfCharacterSprite()
        self.characters_choice_list.append(self.elf_character)
        self.elf_character.visible = False

        self.arrow_left_list = arcade.SpriteList()
        self.arrow_left = ChangeCharacterArrowLeftSprite()
        self.arrow_left_list.append(self.arrow_left)

        self.arrow_right_list = arcade.SpriteList()
        self.arrow_right = ChangeCharacterArrowRightSprite()
        self.arrow_right_list.append(self.arrow_right)

        self.approve_character_button_list = arcade.SpriteList()
        self.approve_character_button = ApproveCharacterButtonSprite()
        self.approve_character_button_list.append(self.approve_character_button)

        self.fullscreen_flag = True

        self.flag_mouse_on_start_button = False

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        arcade.draw_text(self.characters_names[self.current_character_index], self.window.width // 2,
                                   self.window.height * 0.9, arcade.color.WHITE, 40, anchor_x="center", anchor_y="center")
        self.characters_choice_list.draw()
        self.arrow_left_list.draw()
        self.arrow_right_list.draw()
        self.approve_character_button_list.draw()
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

        if button == arcade.MOUSE_BUTTON_LEFT:
            if arcade.get_sprites_at_point((x, y), self.arrow_right_list):
                self.characters_choice_list[self.current_character_index].visible = False
                self.current_character_index += 1
                if self.current_character_index >= len(self.characters_choice_list):
                    self.current_character_index = 0
                    self.characters_choice_list[self.current_character_index].visible = True
                self.characters_choice_list[self.current_character_index].visible = True
            elif arcade.get_sprites_at_point((x, y), self.arrow_left_list):
                self.characters_choice_list[self.current_character_index].visible = False
                self.current_character_index -= 1
                if self.current_character_index < 0:
                    self.current_character_index = len(self.characters_choice_list) - 1
                    self.characters_choice_list[self.current_character_index].visible = True
                self.characters_choice_list[self.current_character_index].visible = True

            if self.approve_character_button.collides_with_point((x, y)):
                main_menu = MainMenu(self.window)
                self.window.show_view(main_menu)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            main_menu = MainMenu(self.window)
            self.window.show_view(main_menu)

        if key == arcade.key.RIGHT or key == arcade.key.D:
            self.characters_choice_list[self.current_character_index].visible = False
            self.current_character_index += 1
            if self.current_character_index >= len(self.characters_choice_list):
                self.current_character_index = 0
                self.characters_choice_list[self.current_character_index].visible = True
            self.characters_choice_list[self.current_character_index].visible = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.characters_choice_list[self.current_character_index].visible = False
            self.current_character_index -= 1
            if self.current_character_index < 0:
                self.current_character_index = len(self.characters_choice_list) - 1
                self.characters_choice_list[self.current_character_index].visible = True
            self.characters_choice_list[self.current_character_index].visible = True



def main():
    window = arcade.Window(width_user, height_user, "Deadly_Hunt")
    window.show_view(MainMenu(window))
    arcade.run()


if __name__ == "__main__":
    main()
