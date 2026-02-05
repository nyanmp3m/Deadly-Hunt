import arcade
from pyglet.graphics import Batch

class DeadScreen(arcade.View):
    def __init__(self, main_view):
        super().__init__()
        self.batch = Batch()
        self.fullscreen_flag = False
        self.main_view = main_view
        self.explanatory_text = arcade.Text("Вы умерли", self.window.width / 2, self.window.height / 2,
                                      arcade.color.WHITE, font_size=40, anchor_x="center", batch=self.batch)

    def on_draw(self):
        self.clear()
        self.batch.draw()

    def on_key_press(self, key, modifier):
        if key == arcade.key.RCTRL:
            if self.fullscreen_flag:
                self.window.set_fullscreen(False)
                self.fullscreen_flag = False
            elif not self.fullscreen_flag:
                self.window.set_fullscreen(True)
                self.fullscreen_flag = True
        if key == arcade.key.SPACE:
            self.window.show_view(self.main_view)
