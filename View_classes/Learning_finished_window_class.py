from fileinput import close

import arcade
from pyglet.graphics import Batch
import View_classes.buffer as buffer_module
class Final(arcade.View):
    def __init__(self, main_view):
        super().__init__()
        self.batch = Batch()
        self.fullscreen_flag = False
        self.main_view = main_view
        if buffer_module.died <= 2:
            self.final_text = arcade.Text("Вы закончили обучение с красным аттестатом", self.window.width / 2,
                                          self.window.height / 2,
                                          arcade.color.WHITE, font_size=40, anchor_x="center", batch=self.batch)
        if 2 < buffer_module.died < 4:
            self.final_text = arcade.Text("Вы закончили обучение с аттестатом", self.window.width / 2,
                                          self.window.height / 2,
                                          arcade.color.WHITE, font_size=40, anchor_x="center", batch=self.batch)
        if buffer_module.died >= 4:
            self.final_text = arcade.Text("Вы закончили обучение со справкой", self.window.width / 2,
                                          self.window.height / 2,
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
            self.window.close()