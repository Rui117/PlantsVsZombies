import time, pygame
from plant.Peashooter import Peashooter
from plant.SunFlower import SunFlower
from plant.Wallnut import Wallnut
from plant.Sun import Sun
from plant.Sun2 import Sun2
from plant.JXC import JXC
from plant.Bullet import Bullet
from plant.Bullet_jxc import Bullet_jxc
from zombie.Zombie import Zombie
from zombie.Zombie_lz import Zombie_lz

# 不建议修改该尺寸，因为所有资源图片都是以该尺寸为前提制作的
pygame.init()
backgd_size = (820, 560)

# 引入资源路径
screen = pygame.display.set_mode(backgd_size)
pygame.display.set_caption("植物大战僵尸")
bg_img_obj = pygame.image.load("../pvz/png/a3.png").convert_alpha()
sunFlowerImg = pygame.image.load("../pvz/png/SunFlower/SunFlower_00.png").convert_alpha()
wallNutImg = pygame.image.load("../pvz/png/Wallnut/Wallnut_00.png").convert_alpha()
peaShooterImg = pygame.image.load("../pvz/png/Peashooter/Peashooter00.png").convert_alpha()
jxcImg = pygame.image.load("../pvz/png/jxc/JXC00.png").convert_alpha()
sunbackImg = pygame.image.load("../pvz/png/SeedBank01.png").convert_alpha()
sunflower_seed = pygame.image.load("../pvz/png/SunFlower_kp.png")
wallnut_seed = pygame.image.load("../pvz/png/Wallnut_kp.png")
peashooter_seed = pygame.image.load("../pvz/png/Peashooter_kp.png")
jxc_seed = pygame.image.load("../pvz/png/jxc_kp.png")


# text为阳光值
text = "500"
sun_font = pygame.font.SysFont("黑体", 25)
sun_num_surface = sun_font.render(str(text), True, (0, 0, 0))
# 定义植物组，子弹组，僵尸组，阳光组
spriteGroup = pygame.sprite.Group()
bulletGroup = pygame.sprite.Group()
zombieGroup = pygame.sprite.Group()
sunsprite = pygame.sprite.Group()

# 定义特殊事件
clock = pygame.time.Clock()
GEN_SUN_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(GEN_SUN_EVENT, 2000)
GEN_BULLET_EVENT = pygame.USEREVENT + 2
pygame.time.set_timer(GEN_BULLET_EVENT, 2000)
GEN_ZOMBIE_EVENT = pygame.USEREVENT + 3
pygame.time.set_timer(GEN_ZOMBIE_EVENT, 10000)
GEN_SUN2_EVENT = pygame.USEREVENT + 4
pygame.time.set_timer(GEN_SUN2_EVENT, 20000)

choose = 0
zombie_num = 0


def main():
    global zombie_num
    global choose
    global text
    global sun_num_surface
    running = True
    index = 0
    while running:
        clock.tick(20)
        for bullet in bulletGroup:
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(bullet, zombie):
                    if isinstance(bullet, Bullet_jxc):
                        zombie.energy -= 2
                        bulletGroup.remove(bullet)
                    else:
                        zombie.energy -= 1
                        bulletGroup.remove(bullet)
        for sprite in spriteGroup:
            for zombie in zombieGroup:
                if pygame.sprite.collide_mask(sprite, zombie):
                    zombie.GOGO = True
                    sprite.zombies.add(zombie)
                if isinstance(sprite, JXC):
                    if abs(zombie.rect.top - sprite.rect[1]) <= 40 and zombie.rect.left < 760:
                        sprite.attack = True
                        if sprite.att == 11:
                            bullet_jxc = Bullet_jxc(sprite.rect, backgd_size, zombie.rect[0])
                            bulletGroup.add(bullet_jxc)
                            break
        '''
            冗余代码，多遍历了一次植物组和僵尸组
            for jxc in spriteGroup:
                for zombie in zombieGroup:
                    if isinstance(jxc, JXC):
                        if abs(zombie.rect.top - jxc.rect[1]) <= 40 and zombie.rect.left < 760:
                            jxc.attack = True
                            if jxc.att == 11:
                                bullet_jxc = Bullet_jxc(jxc.rect, backgd_size, zombie.rect[0])
                                bulletGroup.add(bullet_jxc)
                                break
        '''
        screen.blit(bg_img_obj, (0, 0))
        screen.blit(sunbackImg, (20, 0.5))
        screen.blit(sun_num_surface, (35, 50))
        screen.blit(sunflower_seed, (80, 5))
        screen.blit(peashooter_seed, (121, 5))
        screen.blit(wallnut_seed, (162, 5))
        screen.blit(jxc_seed, (203, 5))
        spriteGroup.update(index)
        spriteGroup.draw(screen)
        bulletGroup.update(index)
        bulletGroup.draw(screen)
        zombieGroup.update(index)
        zombieGroup.draw(screen)
        sunsprite.update(index)
        sunsprite.draw(screen)
        (x, y) = pygame.mouse.get_pos()
        if choose == 1:
            screen.blit(sunFlowerImg, (x - sunFlowerImg.get_rect().width // 2, y - sunFlowerImg.get_rect().height // 2))
        if choose == 2:
            screen.blit(peaShooterImg,
                        (x - peaShooterImg.get_rect().width // 2, y - peaShooterImg.get_rect().height // 2))
        if choose == 3:
            screen.blit(wallNutImg, (x - wallNutImg.get_rect().width // 2, y - wallNutImg.get_rect().height // 2))
        if choose == 4:
            screen.blit(jxcImg, (x - jxcImg.get_rect().width // 2, y - jxcImg.get_rect().height // 2))

        index += 1
        for event in pygame.event.get():
            if event.type == GEN_SUN2_EVENT:
                sun2 = Sun2()
                sunsprite.add(sun2)
            if event.type == GEN_ZOMBIE_EVENT:
                zombie_num += 1
                zombie = Zombie()
                zombie_lz = Zombie_lz()
                if 0 < zombie_num <= 15:
                    zombieGroup.add(zombie)
                if zombie_num > 7:
                    # zombieGroup.add(zombie)
                    zombieGroup.add(zombie_lz)
            if event.type == GEN_SUN_EVENT:
                for sprite in spriteGroup:
                    if isinstance(sprite, SunFlower):
                        now = time.time()
                        if now - sprite.lasttime >= 10:
                            sun = Sun(sprite.rect)
                            sunsprite.add(sun)
                            sprite.lasttime = now
            if event.type == GEN_BULLET_EVENT:
                for sprite in spriteGroup:
                    for zombie in zombieGroup:
                        if isinstance(sprite, Peashooter) \
                                and 0 < sprite.rect[1] - zombie.rect[1] < 50 \
                                and zombie.rect[0] < 760:
                            bullet = Bullet(sprite.rect, backgd_size)
                            bulletGroup.add(bullet)
                            break
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed_key = pygame.mouse.get_pressed()
                if pressed_key[0]:
                    pos = pygame.mouse.get_pos()
                    x, y = pos
                    if 80 <= x < 121 and 5 <= y <= 63 and int(text) >= 50:
                        choose = 1
                    elif 121 <= x < 162 and 5 <= y <= 63 and int(text) >= 100:
                        choose = 2
                    elif 162 <= x < 203 and 5 <= y <= 63 and int(text) >= 50:
                        choose = 3
                    elif 203 <= x < 244 and 5 <= y <= 63 and int(text) >= 100:
                        choose = 4
                    elif 36 < x < 800 and 70 < y < 550:
                        if choose == 1:
                            trueX = x // 90 * 85 + 35
                            trueY = y // 100 * 95 - 15
                            canHold = True
                            for sprite in spriteGroup:
                                if sprite.rect.left == trueX and sprite.rect.top == trueY:
                                    canHold = False
                                    break
                            if not canHold or trueY < 25:
                                break
                            sunflower = SunFlower(time.time(), (trueX, trueY))
                            spriteGroup.add(sunflower)
                            choose = 0
                            text = int(text)
                            text -= 50
                            myfont = pygame.font.SysFont("黑体", 25)
                            sun_num_surface = myfont.render(str(text), True, (0, 0, 0))
                        if choose == 2:
                            trueX = x // 90 * 85 + 32
                            trueY = y // 100 * 95 - 18
                            canHold = True
                            for sprite in spriteGroup:
                                if sprite.rect.left == trueX and sprite.rect.top == trueY:
                                    canHold = False
                                    break
                            if not canHold or trueY < 25:
                                break
                            peashooter = Peashooter((trueX, trueY))
                            spriteGroup.add(peashooter)
                            choose = 0
                            text = int(text)
                            text -= 100
                            myfont = pygame.font.SysFont("黑体", 25)
                            sun_num_surface = myfont.render(str(text), True, (0, 0, 0))
                        if choose == 3:
                            trueX = x // 90 * 85 + 35
                            trueY = y // 100 * 95 - 15
                            canHold = True
                            for sprite in spriteGroup:
                                if sprite.rect.left == trueX and sprite.rect.top == trueY:
                                    canHold = False
                                    break
                            if not canHold or trueY < 25:
                                break
                            wallNut = Wallnut((trueX, trueY))
                            spriteGroup.add(wallNut)
                            choose = 0
                            text = int(text)
                            text -= 50
                            myfont = pygame.font.SysFont("黑体", 25)
                            sun_num_surface = myfont.render(str(text), True, (0, 0, 0))
                        if choose == 4:
                            trueX = x // 90 * 85 + 22
                            trueY = y // 100 * 95 - 35
                            canHold = True
                            for sprite in spriteGroup:
                                if sprite.rect.left == trueX and sprite.rect.top == trueY:
                                    canHold = False
                                    break
                            if not canHold or trueY < 25:
                                break
                            jxc = JXC((trueX, trueY))
                            spriteGroup.add(jxc)
                            choose = 0
                            text = int(text)
                            text -= 100
                            myfont = pygame.font.SysFont("黑体", 25)
                            sun_num_surface = myfont.render(str(text), True, (0, 0, 0))
                    for sun in sunsprite:
                        if sun.rect.collidepoint(pos):
                            sunsprite.remove(sun)
                            text = str(int(text) + 25)
                            sun_font = pygame.font.SysFont("黑体", 25)
                            sun_num_surface = sun_font.render(str(text), True, (0, 0, 0))
            for zombie in zombieGroup:
                if zombie.rect.left == -120:
                    print("你的脑子被僵尸吃了")
                    running = False
                if zombie_num > 20:
                    print("胜利")
                    running = False
        pygame.display.update()


if __name__ == '__main__':
    main()
