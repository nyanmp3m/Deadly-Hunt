import arcade
from pyglet.graphics import Batch
from Sprites_classes.Player_Egor_class import Egor
from View_classes.Dead_screenWindow_class import DeadScreen
import View_classes.buffer as buffer_module
from Sprites_classes.player_EgorB_class import EgorB
from Sprites_classes.ControlPanelSprite_class import ControlPanel
from independentVariables.variables import Cursor_obj
from Sprites_classes.ExplosionSprite_class import Explosion
from Sprites_classes.Gun_sprite_class import Gun
from Sprites_classes.knif_sprite_class import Knife
from Sprites_classes.Rope_sprite_class import Rope
from Sprites_classes.Training_skeleton import Skeleton1
from Sprites_classes.Dice_roll import DiceRoll


SCREEN_TITLE = "Deadly Hunt"
PLAYER_SPEED = 2.5
GRAVITY = 0.75
CAMERA_LERP = 0.12
CAMERA_WIDTH = 600
CAMERA_HEIGHT = 400

width_user, height_user = arcade.get_display_size()

class TrainingLevel(arcade.View):
    def __init__(self):
        super().__init__()
        self.tile_map = arcade.load_tilemap(
            "TrainingLevel/first_location11.tmx",
            scaling=1.5)
        if buffer_module.chosen_player == "white":
            self.player = Egor()
        if buffer_module.chosen_player == "black":
            self.player = EgorB()

        self.control_panel = ControlPanel()
        self.control_panel_list = arcade.SpriteList()
        self.control_panel_list.append(self.control_panel)
        self.player.center_y = self.height / 2
        self.player.center_x = (self.width / 2) * 0.01
        self.player_spawn_point_x = (self.width / 2) * 0.01
        self.player_spawn_point_y = self.height / 2
        self.player_spritelist = arcade.SpriteList()
        self.player_spritelist.append(self.player)
        self.cursor_list = arcade.SpriteList()
        self.cursor = Cursor_obj
        self.cursor_list.append(self.cursor)
        self.explosion_list = arcade.SpriteList()

        self.skeleton1 = Skeleton1()
        self.skeleton_list = arcade.SpriteList()
        self.skeleton_list.append(self.skeleton1)
        self.skeleton1.center_x = (self.width / 2) * 1.4
        self.skeleton1.center_y = self.height / 2

        self.rope = Rope()
        self.rope_list = arcade.SpriteList()
        self.rope_list.append(self.rope)

        self.gun = Gun()
        self.gun_list = arcade.SpriteList()
        self.gun_list.append(self.gun)

        self.knife = Knife()
        self.knife_list = arcade.SpriteList()
        self.knife_list.append(self.knife)

        self.background = arcade.load_texture("TrainingLevel/picture.jpg")

        self.scene = arcade.Scene.from_tilemap(self.tile_map)


        self.score = 0
        self.batch = Batch()

        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.scene["collision"])
        self.physics_engine1 = arcade.PhysicsEngineSimple(self.skeleton1, self.scene["collision"])
        self.world_camera = arcade.camera.Camera2D()
        self.gui_camera = arcade.camera.Camera2D()


        self.camera_shake = arcade.camera.grips.ScreenShake2D(
            self.world_camera.view_data,
            max_amplitude=15.0,
            acceleration_duration=0.1,
            falloff_time=0.5,
            shake_frequency=10.0,
        )

        self.world_width = width_user
        self.world_height = height_user
        self.fullscreen_flag = False


    def on_draw(self):
        self.clear()
        arcade.draw_texture_rect(self.background,
                                 arcade.rect.XYWH(self.width // 2, self.height // 2, self.width, self.height))
        self.control_panel_list.draw()

        self.camera_shake.update_camera()
        self.world_camera.use()
        self.scene.draw()
        self.player_spritelist.draw()
        self.skeleton_list.draw()
        self.camera_shake.readjust_camera()

        self.gui_camera.use()

        self.batch.draw()

        self.knife_list.draw()
        self.rope_list.draw()
        self.gun_list.draw()

        self.explosion_list.draw()
        self.cursor_list.draw()

    def on_update(self, delta_time):
        finished_animation = []
        for i in self.explosion_list:
            i.update_animation(delta_time)
            if i.finished:
                finished_animation.append(i)

        for i in finished_animation:
            self.explosion_list.remove(i)
        if self.player.center_y <= -200:
            dead_screen = DeadScreen(self)
            self.window.show_view(dead_screen)
            self.player.center_y = self.player_spawn_point_y
            self.player.center_x = self.player_spawn_point_x
        self.player.change_y -= GRAVITY
        self.skeleton1.change_y -= GRAVITY

        if self.player.center_y == self.height / 2 and self.player.center_x == (self.width / 2) * 0.01:
            self.how_to_move_text = arcade.Text("D-движение вправо, A-движение влево, W-прыжок, W+D или W+A-рывок",
                                                self.window.width / 2, (self.window.height / 2) * 1.7,
                                                arcade.color.BLACK, font_size=40, anchor_x="center", batch=self.batch)

        if (abs(self.player.center_x -((self.width / 2) * 0.67))) < 15 and (abs(self.player.center_y-((self.height / 2) * 0.35))) < 15:
            self.how_to_move_text = None
            self.game_is_saved = arcade.Text("точка возрождения задана",
                                                self.window.width / 2, (self.window.height / 2) * 1.7,
                                                arcade.color.BLACK, font_size=40, anchor_x="center", batch=self.batch)
            self.player_spawn_point_x = ((self.width / 2) * 0.67)
            self.player_spawn_point_y = ((self.height / 2) * 0.35)
        if (abs(self.player.center_x - ((self.width / 2) * 0.67))) > 15 and (
        abs(self.player.center_y - ((self.height / 2) * 0.35))) > 15:
            self.game_is_saved = None

        self.camera_shake.update(delta_time)
        position = (
            self.player.center_x,
            self.player.center_y
        )
        self.world_camera.position = arcade.math.lerp_2d(
            self.world_camera.position,
            position,
            CAMERA_LERP,
        )

        self.physics_engine.update()
        self.physics_engine1.update()

        check_x = self.player.center_x
        check_y = self.player.center_y - self.player.height / 2 - 5

        items_below = arcade.get_sprites_at_point((check_x, check_y), self.scene["collision"])
        if items_below:
            self.player.jump_count = 0
            self.player.is_jumping = False
        if self.player.is_walking:
            for i in self.player_spritelist:
                i.update_animation(delta_time)
        if self.player.is_jumping:
            for i in self.player_spritelist:
                i.update_animation(delta_time)

        if abs(self.player.center_x - self.skeleton1.center_x) < 50:
            self.player.start_fight()
            dice_roller = DiceRoll()
            roll_result = dice_roller.D20()
            if roll_result < 10:
                self.skeleton1.attack_once()


    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.cursor_list[0].center_x = x
        self.cursor_list[0].center_y = y


    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        explosion = Explosion(x, y + 20)
        self.explosion_list.append(explosion)




    def on_key_press(self, key, modifiers):
        if key == arcade.key.RCTRL:
            if self.fullscreen_flag:
                self.window.set_fullscreen(False)
                self.fullscreen_flag = False
            elif not self.fullscreen_flag:
                self.window.set_fullscreen(True)
                self.fullscreen_flag = True
        if key == arcade.key.W:
            self.player.jump()
        elif key == arcade.key.A:
            self.player.move_left()
        elif key == arcade.key.D:
            self.player.move_right()

    def on_key_release(self, key, modifiers):
        if key in [arcade.key.W]:
            self.player.stop_vertical()

        if key in [arcade.key.A, arcade.key.D]:
            self.player.stop_horizontal()