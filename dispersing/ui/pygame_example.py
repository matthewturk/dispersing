import numpy as np
import sys, pygame
from dispersing.games import TheSummoning

ts = TheSummoning("../../the-summoning/")
speed = [0, 0]
black = 0, 0, 0

pygame.init()

size = width, height = 1024, 768

screen = pygame.display.set_mode(size)


class SpriteDisplay:
    def __init__(self, game, obj_id=0, max_size=400):
        self.game = game
        self.max_size = max_size
        self.switch_obj(obj_id)

    def switch_frame(self, inc):
        self.current_sprite_set
        new_frame_id = self.frame_id + inc
        print("New frame", new_frame_id, len(self.current_sprite_set))
        if new_frame_id >= len(self.current_sprite_set) or new_frame_id < 0:
            return
        self.new_frame_id = new_frame_id
        self._update_sprite(self.current_sprite_set[self.new_frame_id])
        self.sprite.set_palette(palette)

    def switch_obj(self, obj_id):
        if obj_id not in ts.objects:
            return
        print("Switching to obj_id", obj_id)
        self.frame_id = 0
        self.obj_id = obj_id
        _, (_, _, pim) = self.game.objects[obj_id]
        pal1_id, pal2_id, buff = pim
        self.current_sprite_set = buff
        print("nframes: ", len(buff))
        self._update_sprite(buff[0])
        self._set_palette(pal1_id, pal2_id)

    def _update_sprite(self, buff):
        sprite = pygame.image.frombuffer(buff, buff.shape[::-1], "P")
        aspect = buff.shape[1] / buff.shape[0]
        if aspect < 1:
            width = int(self.max_size * aspect)
            height = int(self.max_size)
        else:
            width = int(self.max_size)
            height = int(self.max_size / aspect)
        self.sprite = pygame.transform.scale(sprite, (width, height))
        self.sprite_rect = self.sprite.get_rect()

    def _set_palette(self, pal1_id, pal2_id):
        palette = np.concatenate(
            [self.game.palettes[pal1_id], self.game.palettes[pal2_id]], axis=0
        )
        self._current_palette = palette
        self.sprite.set_palette(palette)


sd = SpriteDisplay(ts)

going = True
while going:
    screen.fill(black)
    screen.blit(sd.sprite, sd.sprite_rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            going = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            sd.switch_obj(sd.obj_id + 1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            sd.switch_obj(sd.obj_id - 1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            sd.switch_frame(1)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            sd.switch_frame(-1)
