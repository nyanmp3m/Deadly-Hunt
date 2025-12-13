import arcade
import random


width_user, height_user = arcade.get_display_size()
images = ["background.png", "background2.png", "background3.png", "background4.png"]
background = random.choice(images)

class DeadlyHunt(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True, fullscreen=False)
        self.background = arcade.load_texture(f"images/{background}")

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))

    def setup(self):
        pass


def main():
    game = DeadlyHunt(width_user, height_user, "Deadly_Hunt")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
