import arcade

width_user, height_user = arcade.get_display_size()

class ChangeCharacterArrowRightSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.6
        self.texture = arcade.load_texture("Pictures/ChangeCharacterArrow_Right.png")
        self.center_x = width_user * 0.9
        self.center_y = height_user // 2