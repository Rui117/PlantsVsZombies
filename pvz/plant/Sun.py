import pygame
import random


class Sun(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(Sun, self).__init__()
        self.image = pygame.image.load("..\pvz\png\Sun\Sun_01.png").convert_alpha()
        self.images = [pygame.image.load("..\pvz\png\Sun\Sun_{:02d}.png".format(i)).convert_alpha()
                       for i in range(1, 14)]
        self.rect = self.images[1].get_rect()
        offsetTop = random.randint(-25, 25)
        offsetleft = random.randint(-25, 25)
        self.rect.top = rect.top + offsetTop
        self.rect.left = rect.left + offsetleft

    def update(self, *args):
        self.image = self.images[args[0] % len(self.images)]
