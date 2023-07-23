# test

## *Назва гри: Лабіринт. Качки проти гусей.*

## *Мета гри: Граючи за качку потрібно знайти шлях через лабіринт, дійти до фінального спрайта (шматка хліба), зібравши по дорозі усі бонуси та не доторкнувшись до спрайтів-ворогів (гусей).*
### *Головний спрайт - качка:*
![image](https://github.com/RenatVed12/test/assets/140271054/fa1012a7-c731-4ca8-b254-daae02a17894)
### *Фінальний спрайт:*
![image](https://github.com/RenatVed12/test/assets/140271054/c5e2c0a1-d171-486f-b0af-345253a6cc92)
### *Спрайт-ворог:*
![image](https://github.com/RenatVed12/test/assets/140271054/09a0d541-0b4b-4a1a-ba3f-b32a58d4d6ee)
## *Елементи керування: керування здійснюється за допомогою стрілок на клавіатурі, а постріл здійснюється за допомогою пробілу (Space).*
> *Елемент коду керування та пострілу:*
```
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
```

## *Особливості:*
### *1. Музичне супроводження*
> *Підключення модуля музичного супроводження та завантаження фонової музики:*
```
mixer.init()
mixer.music.load('назва музичного файлу')
mixer.music.play(-1)
```
> *Завантаження звуків:*
 ```
ytka = mixer.Sound('звук пострілу')
winsound = mixer.Sound('звук перемоги')
losesound = mixer.Sound('звук програшу')
 ```
> *Запуск звуку пострілу:*
```
ytka.play()
```
### *2. Бонуси*
#### *У гру були додані спрайти-бонуси, не зібравши які, гру пройти буде неможливо. Всього бонусів чотири.*
> *Лічильник кількості зібраних бонусів:*

![image](https://github.com/RenatVed12/test/assets/140271054/3d5e1e49-ef4b-434a-8d6a-7159021b0719)

> *Спрайт-бонус:*

![image](https://github.com/RenatVed12/test/assets/140271054/434ad143-ec31-4d6a-9c8b-6915f1eb681b)

### *3. Класи*
#### *За допомогою класів я створював усі спрайти.*
> *Приклад класу:*
```
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
```
> *Приклад використання класу GameSprite для створення стін:*
```
wall1 = GameSprite('wall.png', 530, 100, 50, 820)
```
## *Труднощі:*
### *1. Розміщення спрайтів на ігровій сцені.*
#### *Щоб правильно розмістити всі спрайти потрібно було на око вираховувати координати х та у, запом'ятовувати розташування та назву каждої з 12 спрайтів-стін, щоб правильно відштовхуючись від їхнього розтошування розмістити інші спрайти, потім це все тестити поки спрайти не будуть правильно розташованні. Саме через це, на розміщення спрайтів я витратитив багато часу, але все ж таки зміг правильно розташувати всі спрайтию*\
> *Розміщення на ігровій сцені спрайтів-ворогів, фінального спрайту та головного спрайту:*
```
duck1 = Player(player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed, orien)
final = GameSprite( player_image, player_x, player_y, size_x, size_y)
gys = Enemy_g(player_image, player_x, player_y, size_x, size_y, player_speed, x1, x2)
gys1 = Enemy_g(player_image, player_x, player_y, size_x, size_y, player_speed, x1, x2)
gys2 = Enemy_v(player_image, player_x, player_y, size_x, size_y, player_speed, y1, y2)
```
## *Чим можна доповнити гру у майбутньому:*
### *1. Додати систему рівня складності.*
### *2. Додати декілька рівней.*
### *3. Збільшити кількість ворогів, бонусів та сніт.*

















