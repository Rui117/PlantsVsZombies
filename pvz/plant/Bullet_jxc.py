import pygame


class Bullet_jxc(pygame.sprite.Sprite):
    def __init__(self, JXC_rect, backgd_size, life1):
        super(Bullet_jxc, self).__init__()
        self.image = pygame.image.load('../pvz/png/bullet_0.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = JXC_rect[0] + 50
        self.rect.top = JXC_rect[1]
        self.width = backgd_size[0]
        self.life2 = int(life1 / 120) - int(JXC_rect[1] / 200) - 4
        self.speed = 10 + self.life2
        self.a = 0

    def update(self, *args, **kwargs) -> None:
        if self.rect.right < self.width:
            self.rect.left += self.speed
            if self.a < 100:
                y = 12 - self.a
                self.rect.top -= int(y)
                self.a += 0.5
        else:
            self.kill()
