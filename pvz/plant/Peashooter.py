import pygame


class Peashooter(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(Peashooter, self).__init__()
        self.image = pygame.image.load("..\pvz\png\Peashooter\Peashooter_00.png").convert_alpha()
        self.images = [pygame.image.load("..\pvz\png\Peashooter\Peashooter_{:02d}.png".format(i)).convert_alpha()
                       for i in range(0, 25)]
        self.rect = self.images[0].get_rect()
        self.rect.left = rect[0]
        self.rect.top = rect[1]
        self.energy = 60
        self.zombies = set()

    def update(self, *args):
        for zombie in self.zombies:
            if not zombie.Alive:
                self.energy += 0
            else:
                self.energy -= 1
        if self.energy <= 0:
            for zombie in self.zombies:
                zombie.GOGO = False
            self.kill()
        self.image = self.images[args[0] % len(self.images)]
