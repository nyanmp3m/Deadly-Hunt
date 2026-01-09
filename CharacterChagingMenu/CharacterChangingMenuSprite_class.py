import arcade

from Sprites_classes.KnightCharacterSprite_class import KnightCharacterSprite
from Sprites_classes.ChangeCharacterArrowLeftSprite_class import ChangeCharacterArrowLeftSprite
from Sprites_classes.ChangeCharacterArrowRightSprite_class import ChangeCharacterArrowRightSprite
from Sprites_classes.GnomeCharacterSprite_class import GnomeCharacterSprite
from Sprites_classes.SamuraiCharacterSprite_class import SamuraiCharacterSprite
from Sprites_classes.ApproveCharacterButtonSprite_class import ApproveCharacterButtonSprite
from Sprites_classes.Cursor_texture import Cursor


width_user, height_user = arcade.get_display_size()

class CharacterChangeView(arcade.View):
    def __init__(self, window):
        super().__init__(window)
        self.background = arcade.color.DARK_GREEN
        self.window = window
        self.fullscreen = False
        arcade.set_background_color(self.background)
        self.cursor_list = arcade.SpriteList()

        self.cursor = Cursor(width_user // 2, height_user // 2)
        self.cursor_list.append(self.cursor)

        self.characters_choice_list = arcade.SpriteList()
        self.current_character_index = 0
        self.characters_names = ["Рыцарь", "Гном", "Самурай"]

        self.knight_character = KnightCharacterSprite()
        self.characters_choice_list.append(self.knight_character)
        self.knight_character.visible = True

        self.gnome_character = GnomeCharacterSprite()
        self.characters_choice_list.append(self.gnome_character)
        self.gnome_character.visible = False

        self.samurai_character = SamuraiCharacterSprite()
        self.characters_choice_list.append(self.samurai_character)
        self.samurai_character.visible = False

        self.arrow_left_list = arcade.SpriteList()
        self.arrow_left = ChangeCharacterArrowLeftSprite()
        self.arrow_left_list.append(self.arrow_left)

        self.arrow_right_list = arcade.SpriteList()
        self.arrow_right = ChangeCharacterArrowRightSprite()
        self.arrow_right_list.append(self.arrow_right)

        self.approve_character_button_list = arcade.SpriteList()
        self.approve_character_button = ApproveCharacterButtonSprite()
        self.approve_character_button_list.append(self.approve_character_button)


    def on_draw(self):
        self.clear()
        self.characters_choice_list.draw()
        self.arrow_left_list.draw()
        self.arrow_right_list.draw()
        self.approve_character_button_list.draw()
        self.cursor_list.draw()

    def on_update(self, delta_time):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        self.cursor_list[0].center_x = x
        self.cursor_list[0].center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
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
                from StartingWindow.StartingWindow import MainMenu
                main_menu = MainMenu(self.window)
                self.window.show_view(main_menu)