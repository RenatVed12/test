# Розроби свою гру в цьому файлі!
from pygame import *
mixer.init()
font.init()
mixer.music.load('music.mp3')
mixer.music.play(-1)
ytka = mixer.Sound('ytka.wav')
winsound = mixer.Sound('win.wav')
losesound = mixer.Sound('lose.wav')

win_width = 1000
win_height = 800
window = display.set_mode((win_width, win_height))
display.set_caption('Лабіринт. Утки против гусей. Битва за хлебушек.')
background = transform.scale(image.load('lake.jpg'), (1000, 800))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def  __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed, orien):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
        self.orien = orien
    def update(self):
        if duck1.rect.x <= win_width-80 and duck1.x_speed > 0 or duck1.rect.x >= 0 and duck1.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if duck1.rect.y <= win_height-80 and duck1.y_speed > 0 or duck1.rect.y >= 0 and duck1.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def draw(self):
        if self.orien == 'right':
            window.blit(self.image,(self.rect.x, self.rect.y))
        elif self.orien == 'left':
            window.blit(transform.flip(self.image, True, False), (self.rect.x,self.rect.y))
    def fire(self):
        if self.orien == 'right':
            bullets.add(Bullet('bullet.png', self.rect.right, self.rect.centery,15,20,15))
        elif self.orien == 'left':
            bullets.add(Bullet('bullet.png', self.rect.left, self.rect.centery,15,20, -15))
           

class Enemy_g(GameSprite):
    side = 'left'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, x1, x2):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.x1 = x1
        self.x2 = x2
    def update(self):
        if self.rect.x <= self.x1:
            self.side = "right"
        if self.rect.x >= self.x2:
            self.side = "left"
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
        
class Enemy_v(GameSprite):
    side = 'top'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, y1, y2):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.y1 = y1
        self.y2 = y2
    def update(self):
        if self.rect.y <= self.y1:
            self.side = "bottom"
        if self.rect.y >= self.y2:
            self.side = "top"
        if self.side == 'top':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width + 10:
            self.kill()
        elif self.rect.x < 0:
            self.kill()




        
barriers = sprite.Group()

bullets = sprite.Group()

gysi = sprite.Group()

bonus = sprite.Group()


wall1 = GameSprite('wall.png', 530, 100, 50, 820)
wall2 = GameSprite('wall.png', 400, 400, 300, 50 )
wall3 = GameSprite('wall.png', 700, 250, 210, 50 )
wall4 = GameSprite('wall.png', -20, 100, 450, 50 )
wall5 = GameSprite('wall.png', 200, 120, 50, 350 )
wall6 = GameSprite('wall.png', 200, 600, 700, 50 )
wall7 = GameSprite('wall.png', 830, 100, 50, 600)
wall8 =  GameSprite('wall.png', 230, 245, 150, 50)
wall9 = GameSprite('wall.png', 970, 400, 100, 50 )
wall10 = GameSprite('wall.png', 780, 630, 50, 50)
wall11 = GameSprite('wall.png', 250, 80, 50, 50)
wall12 = GameSprite('wall.png', 100, -30 , 50, 50)
barriers.add(wall1)
barriers.add(wall2)
barriers.add(wall3)
barriers.add(wall4)
barriers.add(wall5)
barriers.add(wall6)
barriers.add(wall7)
barriers.add(wall8)
barriers.add(wall9)
barriers.add(wall10)
barriers.add(wall11)
barriers.add(wall12)

font1 = font.SysFont('arial', 25)

bonus_amount = 0
bonus1 = GameSprite('bonusk.png', 600, 500, 70,70)
bonus2 = GameSprite('bonusk.png', 400, 680, 70,70)
bonus3 = GameSprite('bonusk.png', 10, 25, 70,70)
bonus4 = GameSprite('bonusk.png', 270, 160, 70,70)

duck1 = Player('duck.png', 650, 680, 80, 80, 0, 0, 'left' )
final = GameSprite('finalsp.png', 60, 160, 80,80)
gys = Enemy_g('gys1.png', 150, 480, 80,80, 5, 30, 400)
gys1 = Enemy_g('gys1.png', 500, 15, 80,80, 5, 300, 900)
gys2 = Enemy_v('gys1.png', 590, 200, 80,80, 5, 100, 320)

bonus.add(bonus1)
bonus.add(bonus2)
bonus.add(bonus3)
bonus.add(bonus4)


gysi.add(gys)
gysi.add(gys1)
gysi.add(gys2)


finish = False
run = True
while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                duck1.x_speed = -5
            elif e.key == K_RIGHT:
                duck1.x_speed = 5
            elif e.key == K_UP:
                duck1.y_speed = -5
            elif e.key == K_DOWN:
                duck1.y_speed = 5
            elif e.key == K_SPACE:
                duck1.fire()
                ytka.play()
        elif e.type == KEYUP:
            if e.key == K_LEFT:
                duck1.x_speed = 0
            elif e.key == K_RIGHT:
                duck1.x_speed = 0
            elif e.key == K_UP:
                duck1.y_speed = 0
            elif e.key == K_DOWN:
                duck1.y_speed = 0
    
    

    if finish != True:
        window.blit(background, (0,0))
        barriers.draw(window)
        duck1.reset()
        final.reset()
        duck1.update()
        bullets.draw(window)
        bullets.update() 
        gysi.update()
        gysi.draw(window)
        sprite.groupcollide(gysi, bullets, True, True)
        sprite.groupcollide(bullets, barriers, True, False)
        bonus.draw(window)
        if sprite.spritecollide(duck1, bonus, True):
            bonus_amount += 1
        bonusy = font1.render(f'Бонусів: {bonus_amount}/4', True, (0,0,0))
        window.blit(bonusy, (10,10))
        

        if sprite.spritecollide(duck1, gysi, False):
            finish = True
            mixer.music.stop()
            losesound.play()
            img = image.load('defeat.jpg')
            window.blit(transform.scale(img, (1000, 800)), (0,0))
        
        if sprite.collide_rect(duck1, final) and bonus_amount == 4:
            finish = True
            mixer.music.stop()
            winsound.play()
            window.blit(transform.scale(image.load('win.jpg'), (1000, 800)), (0, 0))
            #window.blit(win, (0,0))





    display.update()

