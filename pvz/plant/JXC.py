import pygame


class JXC(pygame.sprite.Sprite):
    def __init__(self, rect):
        super(JXC, self).__init__()
        self.image = pygame.image.load("..\pvz\png\jxc\JXC_00.png").convert_alpha()
        self.images1 = [pygame.image.load("..\pvz\png\jxc\JXC_{:02d}.png".format(i)).convert_alpha() for i in
                        range(0, 31)]
        self.images2 = [pygame.image.load("..\pvz\png\jxc\JXC_{:02d}.png".format(i)).convert_alpha() for i in
                        range(31, 69)]
        self.rect = self.images1[0].get_rect()
        self.rect.left = rect[0]
        self.rect.top = rect[1]
        self.energy = 60
        self.zombies = set()
        self.attack = False
        self.att = 0

    def update(self, *args):
        if not self.attack:
            self.image = self.images1[args[0] % len(self.images1)]
        elif self.attack:
            if self.att < 38:
                self.image = self.images2[self.att]
                self.att += 1
            else:
                self.att = 0
                self.attack = False
        for zombie in self.zombies:
            if not zombie.Alive:
                self.energy += 0
            else:
                self.energy -= 1
        if self.energy <= 0:
            for zombie in self.zombies:
                zombie.GOGO = False
            self.kill()
