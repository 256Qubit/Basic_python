import pygame
import sys
import random


# 初始化Pygame
pygame.init()

# 游戏设置
WIDTH, HEIGHT = 800, 600
FPS = 60

# 颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 玩家坦克
player_tank = pygame.Rect(50, 50, 50, 50)
player_speed = 5
player_bullet_speed = 10

# 敌人坦克
enemy_tank = pygame.Rect(700, 500, 50, 50)
enemy_speed = 2
enemy_bullet_speed = 5

# 子弹
player_bullets = []
enemy_bullets = []

# 设置窗口
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank Battle")
clock = pygame.time.Clock()

def draw_tank(rect, color):
    pygame.draw.rect(screen, color, rect)

def draw_bullets(bullets, color):
    for bullet in bullets:
        pygame.draw.rect(screen, color, bullet)

def check_collision(bullets, tank):
    for bullet in bullets:
        if tank.colliderect(bullet):
            return True
    return False

# 游戏循环
running = True
while running:
    clock.tick(FPS)

    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取键盘输入
    keys = pygame.key.get_pressed()

    # 移动玩家坦克
    if keys[pygame.K_w] and player_tank.top > 0:
        player_tank.y -= player_speed
    if keys[pygame.K_s] and player_tank.bottom < HEIGHT:
        player_tank.y += player_speed
    if keys[pygame.K_a] and player_tank.left > 0:
        player_tank.x -= player_speed
    if keys[pygame.K_d] and player_tank.right < WIDTH:
        player_tank.x += player_speed

    # 发射玩家子弹
    if keys[pygame.K_SPACE]:
        player_bullet = pygame.Rect(player_tank.centerx - 5, player_tank.y, 10, 20)
        player_bullets.append(player_bullet)

    # 移动敌人坦克
    if enemy_tank.x < player_tank.x:
        enemy_tank.x += enemy_speed
    elif enemy_tank.x > player_tank.x:
        enemy_tank.x -= enemy_speed
    if enemy_tank.y < player_tank.y:
        enemy_tank.y += enemy_speed
    elif enemy_tank.y > player_tank.y:
        enemy_tank.y -= enemy_speed

    # 发射敌人子弹
    if random.randint(0, 100) < 5:
        enemy_bullet = pygame.Rect(enemy_tank.centerx - 5, enemy_tank.y + 50, 10, 20)
        enemy_bullets.append(enemy_bullet)

    # 移动玩家子弹
    for bullet in player_bullets:
        bullet.y -= player_bullet_speed
        if bullet.y < 0:
            player_bullets.remove(bullet)

    # 移动敌人子弹
    for bullet in enemy_bullets:
        bullet.y += enemy_bullet_speed
        if bullet.y > HEIGHT:
            enemy_bullets.remove(bullet)

    # 检查子弹和坦克碰撞
    if check_collision(player_bullets, enemy_tank):
        print("Player wins!")
        running = False

    if check_collision(enemy_bullets, player_tank):
        print("Enemy wins!")
        running = False

    # 绘制
    screen.fill(WHITE)
    draw_tank(player_tank, RED)
    draw_tank(enemy_tank, BLUE)
    draw_bullets(player_bullets, RED)
    draw_bullets(enemy_bullets, BLUE)

    pygame.display.flip()

pygame.quit()
sys.exit()
