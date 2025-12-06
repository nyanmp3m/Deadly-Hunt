import arcade

width_user, height_user = arcade.get_display_size()


class MainWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False, fullscreen=True)
        self.background_color = arcade.color.TEA_GREEN

    def setup(self):
        pass

    def on_draw(self):
        self.clear()


def main():
    game = MainWindow(width_user, height_user, "Deadly_Hunt")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
