import pygame
import sys

# 初始化 Pygame
pygame.init()

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 定义屏幕大小
screen_width = 800
screen_height = 600

# 创建屏幕对象
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tank Battle Game")

# 定义坦克
tank_size = 50
tank_x = screen_width // 2 - tank_size // 2
tank_y = screen_height - tank_size - 10

# 设置坦克速度
tank_speed = 5

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 获取按键状态
    keys = pygame.key.get_pressed()

    # 移动坦克
    if keys[pygame.K_LEFT] and tank_x > 0:
        tank_x -= tank_speed
    if keys[pygame.K_RIGHT] and tank_x < screen_width - tank_size:
        tank_x += tank_speed
    if keys[pygame.K_UP] and tank_y > 0:
        tank_y -= tank_speed
    if keys[pygame.K_DOWN] and tank_y < screen_height - tank_size:
        tank_y += tank_speed

    # 清屏
    screen.fill(BLACK)

    # 绘制坦克
    pygame.draw.rect(screen, WHITE, [tank_x, tank_y, tank_size, tank_size])

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    pygame.time.Clock().tick(30)
