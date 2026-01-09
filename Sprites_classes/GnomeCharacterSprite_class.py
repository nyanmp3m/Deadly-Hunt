import arcade

width_user, height_user = arcade.get_display_size()

class GnomeCharacterSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 3
        self.texture = arcade.load_texture("Pictures/Characters/Gnome_Character.png")
        self.center_x = width_user // 2
        self.center_y = height_user // 2