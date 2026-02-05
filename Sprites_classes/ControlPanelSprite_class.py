import arcade

width_user, height_user = arcade.get_display_size()

class ControlPanel(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.scale = 1

        self.texture = arcade.load_texture("TrainingLevel/controlPanel.png")
        self.center_x = width_user // 2
        self.center_y = height_user * 0.15