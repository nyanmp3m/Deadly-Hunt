import arcade

width_user, height_user = arcade.get_display_size()

class ChangeCharacterArrowLeftSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 0.6
        self.texture = arcade.load_texture("Pictures/ChangeCharacterArrow_Left.png")
        self.center_x = width_user * 0.1
        self.center_y = height_user // 2