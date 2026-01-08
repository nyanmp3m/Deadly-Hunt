import arcade

width_user, height_user = arcade.get_display_size()

class KnightCharacterSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 2.5
        self.texture = arcade.load_texture("Pictures/Characters/Knight_Character.png")
        self.center_x = width_user // 2
        self.center_y = height_user // 2