import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, Peashooter_rect, backgd_size):
        super(Bullet, self).__init__()
        self.image = pygame.image.load('../pvz/png/BulletPea1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = Peashooter_rect[0] + 65
        self.rect.top = Peashooter_rect[1] + 13
        self.width = backgd_size[0]
        self.speed = 6

    def update(self, *args, **kwargs) -> None:
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.kill()
