import pygame
import sys
import math
import random

# 初始化 Pygame
pygame.init()

# 設置遊戲窗口大小
window_width = 1280
window_height = 800
window_size = (window_width, window_height)

# 色彩
BLACK = (0, 0, 0)

# 創建遊戲窗口
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("坦克大作戰")

# 定義遊戲結束函數
def game_over():
    print("Game Over")  # 示例：打印游戏结束
    pygame.quit()
    sys.exit()

# 定義任務成功函數
def mission_success():
    print("Mission Success!")  # 示例：打印任务成功
    pygame.quit()
    sys.exit()

# 定義玩家坦克類別
class PlayerTank(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.original_image = image
        self.image = self.original_image
        self.rect = self.image.get_rect(center=position)
        self.angle = 0
        self.speed = 2  # 調整坦克速度
        self.bullets = pygame.sprite.Group()  # 創建子彈群組
        self.shoot_delay = 100  # 设定射击延迟时间
        self.shoot_timer = 0  # 射击计时器
        self.is_player = True  # 添加一个属性标识玩家

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keys = pygame.key.get_pressed()

        # 單方向移動
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.speed_x = -self.speed
            self.angle = 90
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.speed_x = self.speed
            self.angle = 270
        elif keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.speed_y = -self.speed
            self.angle = 0
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.speed_y = self.speed
            self.angle = 180

        # 移動前暫存原始位置
        old_x = self.rect.x
        old_y = self.rect.y

        # 移動
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 檢查碰撞
        if self.rect.left < 0 or self.rect.right > window_width or self.rect.top < 0 or self.rect.bottom > window_height:
            # 如果超出邊界，恢復到移動之前的位置
            self.rect.x = old_x
            self.rect.y = old_y

        self.rotate()

        # 更新子彈
        self.bullets.update()

        # 射击计时器更新
        self.shoot_timer += 1

    def rotate(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        # 繪製子彈
        self.bullets.draw(screen)

    def shoot(self):
        if self.shoot_timer >= self.shoot_delay:
            # 計算子彈的初始位置
            bullet_position = (
                self.rect.centerx + math.cos(math.radians(self.angle - 90)) * 30,
                self.rect.centery - math.sin(math.radians(self.angle - 90)) * 30
            )

            # 創建一個子彈對象並添加到子彈群組中
            bullet = Bullet(bullet_position, self.angle)
            self.bullets.add(bullet)
            self.shoot_timer = 0  # 重置射击计时器

# 定義子彈類別
class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, angle):
        super().__init__()
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect(center=position)
        self.angle = angle
        self.speed = 5
        self.collide_count = 0  # 记录碰撞次数
        self.is_enemy_bullet = False  # 标记是否为敌人发射的子弹

    def update(self):
        angle_rad = math.radians(self.angle - 90)
        self.rect.x -= self.speed * math.cos(angle_rad)
        self.rect.y += self.speed * math.sin(angle_rad)

        # 检查子弹是否碰到玩家坦克
        if self.rect.colliderect(player_tank.rect) and not player_tank.is_player:
            # 子弹碰到玩家坦克，玩家坦克消失，游戏结束
            player_tank.kill()
            game_over()

        # 如果是敌人发射的子弹，则排除与发射子弹的坦克的碰撞检测
        if not self.is_enemy_bullet:
            # 检查子弹是否碰到敌人坦克
            enemy_hit_list = pygame.sprite.spritecollide(self, enemies, False)
            for enemy in enemy_hit_list:
                # 排除发射子弹的敌人
                if enemy.is_enemy:
                    self.collide_count += 1
                    if self.collide_count >= 3:
                        enemy.kill()  # 敌人坦克消失
                        self.kill()  # 子弹消失
                        self.collide_count = 0  # 重置碰撞次数

        # 检查是否所有敌人坦克都消失了
        if len(enemies) == 0:
            mission_success()

        # 检查子弹是否超出游戏窗口，如果是则删除子弹对象
        if not pygame.Rect(0, 0, window_width, window_height).colliderect(self.rect):
            self.kill()

# 定義敵人坦克類別
class EnemyTank(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.original_image = image
        self.image = self.original_image
        self.rect = self.image.get_rect(center=position)
        self.angle = random.choice([0, 90, 180, 270])
        self.speed = 2
        self.shoot_timer = 0
        self.shoot_delay = 60
        self.is_enemy = True  # 添加一个属性标识敌人

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        
        # 單方向移動，與玩家坦克相同
        if random.randint(0, 100) < 3:
            self.angle = random.choice([0, 90, 180, 270])
        
        if self.angle == 0:
            self.speed_y = -self.speed
            self.image = pygame.transform.rotate(self.original_image, 0)
        elif self.angle == 90:
            self.speed_x = -self.speed
            self.image = pygame.transform.rotate(self.original_image, 90)
        elif self.angle == 180:
            self.speed_y = self.speed
            self.image = pygame.transform.rotate(self.original_image, 180)
        elif self.angle == 270:
            self.speed_x = self.speed
            self.image = pygame.transform.rotate(self.original_image, 270)

        # 移動
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # 檢查是否超出邊界，並調整位置
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > window_width:
            self.rect.right = window_width
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > window_height:
            self.rect.bottom = window_height

        # 射擊
        self.shoot_timer += 1
        if self.shoot_timer >= self.shoot_delay:
            self.shoot()
            self.shoot_timer = 0

    def shoot(self):
        # 计算子弹的初始位置
        bullet_position = (
            self.rect.centerx + math.cos(math.radians(self.angle - 90)) * 30,
            self.rect.centery - math.sin(math.radians(self.angle - 90)) * 30
        )

        # 创建一个子弹对象并添加到子弹群组中
        bullet = Bullet(bullet_position, self.angle)
        bullets.add(bullet)

        # 标记子弹为发射的子弹
        bullet.is_enemy_bullet = True

# 加載玩家坦克的圖像
try:
    player_tank_image = pygame.image.load("player_tank.png")
except pygame.error as e:
    print(f"Cannot load image: {e}")
    pygame.quit()
    sys.exit()

# 創建玩家坦克對象
player_tank = PlayerTank(player_tank_image, (window_width // 2, window_height // 2))

# 加載敵人坦克的圖像
try:
    enemy_tank_image = pygame.image.load("enemy_tank.png")
except pygame.error as e:
    print(f"Cannot load image: {e}")
    pygame.quit()
    sys.exit()

# 創建敵人坦克群組
enemies = pygame.sprite.Group()

# 創建敵人坦克
for _ in range(7):
    enemy = EnemyTank(enemy_tank_image, (random.randint(0, window_width), random.randint(0, window_height)))
    enemies.add(enemy)

# 創建子彈群組
bullets = pygame.sprite.Group()

# 主遊戲循環
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 監聽按鍵事件，如果按下空白鍵則射擊
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_tank.shoot()

    # 更新玩家坦克
    player_tank.update()

    # 更新敵人坦克
    enemies.update()

    # 更新子彈
    bullets.update()

    # 检查敌人子弹是否击中玩家坦克
    enemy_bullet_hit_player = pygame.sprite.spritecollide(player_tank, bullets, True)
    if enemy_bullet_hit_player:
        game_over()

    # 清除畫面
    screen.fill(BLACK)

    # 繪製玩家坦克
    player_tank.draw(screen)

    # 繪製敵人坦克
    enemies.draw(screen)

    # 繪製子彈
    bullets.draw(screen)

    # 畫面更新
    pygame.display.flip()

    # 控制幀率
    clock.tick(60)

# 退出遊戲
pygame.quit()
sys.exit()

