from pygame import *
from random import *
from time import time as timer
from time import sleep
window = display.set_mode((700, 500))
display.set_caption("Ping-pong")
background = transform.scale(image.load("ping-pong_table.jpg"), (700, 500))

finish = False
font.init()
font = font.Font(None, 30)

clock = time.Clock()
FPS = 60

mixer.init()
#mixer.music.load("galaxy.ogg")
#mixer.music.play()
#shoot = mixer.Sound("fire.ogg")

class GameSprate(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprate):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed


player_r = Player("raketka1.png", 625, 400, 80, 100, 10)
player_l = Player("raketka2.png", 1, 400, 80, 100, 10)
ball = GameSprate("miyach.png", 330, 220, 60, 70, 10)
game = True
speed_x = 3
speed_y = 3
lose1 = font.render(input("Введите ваше имя:") + "You Suck", True, (180, 0, 0))
lose2 = font.render(input("Введите ваше имя:") + "You Suck", True, (180, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0, 0))
        player_r.update_r()
        player_l.update_l()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(player_r, ball) or sprite.collide_rect(player_l, ball):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.y > 430 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < -70:
            finish = True
            window.blit(lose1, (0, 0))
            game_over = True
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (0, 0))
            game_over = True

        player_r.reset()
        player_l.reset()
        ball.reset()
         
    clock.tick(FPS)
    display.update()