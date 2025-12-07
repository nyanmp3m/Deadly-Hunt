import arcade


class SettingsSprite(arcade.Sprite):
    def __init__(self):
        super().__init__('Pictures/SettingsSprite_picture.png')
        self.speed = 0