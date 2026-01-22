import arcade

width_user, height_user = arcade.get_display_size()


class SamuraiCharacterSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 2
        self.texture = arcade.load_texture("Pictures/Characters/Samurai_Character.png")
        self.center_x = width_user // 2
        self.center_y = height_user // 2
