import arcade

width_user, height_user = arcade.get_display_size()

class SettingsSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.scale = 0.25
        self.speed = 0
        self.health = 1

        self.idle_texture = arcade.load_texture("Pictures/SettingsSprite_picture.png")
        self.texture = self.idle_texture

        self.center_x = width_user // 2
        self.center_y = height_user // 2