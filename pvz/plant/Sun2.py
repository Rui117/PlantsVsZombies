import pygame
import random


class Sun2(pygame.sprite.Sprite):
    def __init__(self):
        super(Sun2, self).__init__()
        self.image = pygame.image.load("..\pvz\png\Sun\Sun_01.png").convert_alpha()
        self.images = [pygame.image.load("..\pvz\png\Sun\Sun_{:02d}.png".format(i)).convert_alpha()
                       for i in range(1, 14)]
        self.rect = self.images[1].get_rect()
        self.rect.left = random.randint(50, 720)
        self.rect.top = -50
        self.speed = 2

    def update(self, *args):
        self.image = self.images[args[0] % len(self.images)]
        if self.rect.bottom < 560:
            self.rect.top += self.speed
