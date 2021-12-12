from pygame import *
import pygame_menu
init()

w_width = 700
w_height = 600
window = display.set_mode((w_width,w_height))
display.set_caption("ping-pong")
clock = time.Clock()

speed_x = 7
speed_y = 7


racket_height = 50

ball_h_w = 25

def set_difficulty(*args):
    global speed_x, speed_y, racket_height, ball_h_w

    if args[1] == 3:
        speed_x = 5
        speed_y = 2
        racket_height = 95
        ball_h_w = 50
    if args[1] == 2:
        speed_x = 2
        speed_y = 1
        racket_height = 115
        ball_h_w = 75
    if args[1] == 1:
        speed_x = 10
        speed_y = 7
        racket_height = 50
        ball_h_w = 25

def start_the_game():
    run = True
    game = True
    finish = False

    #background = transform.scale(image.load("galaxy.jpg"), (w_width,w_height))

    lost = 0
    max_lost=2

    #Font.init()
    font1 = font.SysFont('ComicSansMC', 50)
    win1 = font1.render(
        'Игрок 1 победил', True, (0, 0, 0)
    )
    win2 = font1.render(
        'Игрок 2 победил', True, (0, 0, 0)
    )
    class GameSprite(sprite.Sprite):
        def __init__(self, playerimage, playerx, playery, spr_width, spr_height, playerspeed):
            super().__init__()
            self.image = transform.scale(image.load(playerimage), (spr_height, spr_width))
            self.speed = playerspeed
            self.rect = self.image.get_rect()
            self.rect.x = playerx
            self.rect.y = playery
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))
    class Racket(GameSprite):
        def update_l(self):
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < 500:
                self.rect.y += self.speed
        def update_r(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 500:
                self.rect.y += self.speed
        def update_ball(self):
            global speed_x
            global speed_y
            self.rect.x += speed_x
            self.rect.y += speed_y
            if self.rect.y > w_height-50 or self.rect.y < 0:
                speed_y *= -1
            if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket2, ball):
                speed_x *= -1
    '''class T_ball(GameSprite):
        def update_ball(self):
            self.rect.x += speed_x
            self.rect.y += speed_y
            if self.rect.y > w_height-50
                or self.rect.y < 0:
                speed_y *= -1'''

    racket = Racket("racket.png", 630, 250, racket_height, 25, 10)
    racket2 = Racket("racket2.png", 20, 250, racket_height, 25, 10)
    ball = Racket("tenis_ball.png", 350, 300, ball_h_w, ball_h_w, 3)
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
        if not finish:
            window.fill((255, 165, 0))
            # ball.rect.x += speed_x
            # ball.rect.y += speed_y
            racket.update_l()
            racket.reset()
            racket2.update_r()
            racket2.reset()
            ball.update_ball()
            ball.reset()
            
            
            #ball.rect.x += speed_x
            #ball.rect.y += speed_y



            if ball.rect.x < 0:
                finish = True
                window.blit(win1, (200,200))
            if ball.rect.x > 680:
                finish = True
                window.blit(win2, (200,200))
        display.update()
        clock.tick(60)
menu = pygame_menu.Menu("Привет-привет", 350, 300, theme = pygame_menu.themes.THEME_SOLARIZED)
menu.add.selector('Difficulty', [('Hard', 1), ("Easy", 2), ("Normal", 3)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT) 
menu.mainloop(window)