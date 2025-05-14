import pygame
import math

# Настройки окна
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Чёрный фон
LINE_COLOR = (255, 255, 255)  # Белые линии

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Куб (исправлено)")
clock = pygame.time.Clock()

# Вершины куба (x, y, z)
vertices = [
    (-1, -1, -1),  # 0
    (1, -1, -1),  # 1
    (1, 1, -1),  # 2
    (-1, 1, -1),  # 3
    (-1, -1, 1),  # 4
    (1, -1, 1),  # 5
    (1, 1, 1),  # 6
    (-1, 1, 1)  # 7
]

# Рёбра (соединяем вершины)
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),  # Задняя грань
    (4, 5), (5, 6), (6, 7), (7, 4),  # Передняя грань
    (0, 4), (1, 5), (2, 6), (3, 7)  # Соединяющие рёбра
]


def project(point, angle_x, angle_y, scale=150, distance=5):
    """Преобразует 3D-точку в 2D-координаты с учётом вращения"""
    x, y, z = point

    # Вращение вокруг оси Y (горизонтальное)
    new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
    new_z = x * math.sin(angle_y) + z * math.cos(angle_y)

    # Вращение вокруг оси X (вертикальное)
    new_y = y * math.cos(angle_x) - new_z * math.sin(angle_x)
    new_z_final = y * math.sin(angle_x) + new_z * math.cos(angle_x)

    # Перспективная проекция
    factor = scale / (distance + new_z_final)  # distance — расстояние от камеры
    screen_x = new_x * factor + WIDTH // 2
    screen_y = -new_y * factor + HEIGHT // 2

    return (int(screen_x), int(screen_y))


# Основной цикл
angle_x, angle_y = 0, 0
running = True

while running:
    screen.fill(BACKGROUND_COLOR)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Увеличиваем углы для анимации вращения
    angle_x += 0.01
    angle_y += 0.02



    # Рисуем все рёбра куба
    for edge in edges:
        start_vertex = vertices[edge[0]]
        end_vertex = vertices[edge[1]]

        start_pos = project(start_vertex, angle_x, angle_y)
        end_pos = project(end_vertex, angle_x, angle_y)

        pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos, 2)

    pygame.display.flip()
    clock.tick(60)  # 60 FPS

pygame.quit()