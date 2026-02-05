import arcade

PLAYER_SPEED = 2.5
GRAVITY = 0.75

class Egor(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.player = arcade.Sprite(
            "TrainingLevel/Egor.png",
            scale=0.1)
        self.player.center_y = self.height / 2
        self.player.center_x = (self.width / 2) - 950
        self.player_spritelist = arcade.SpriteList()
        self.player_spritelist.append(self.player)

    def on_update(self, delta_time):
        self.player.change_y -= GRAVITY

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED * 3
        elif key == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN]:
            self.player.change_y = 0
        if key in [arcade.key.LEFT, arcade.key.RIGHT]:
            self.player.change_x = 0
