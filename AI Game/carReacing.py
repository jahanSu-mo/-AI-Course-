import pygame
import os
import random
import heapq

# === Initialize ===
pygame.init()
WIDTH, HEIGHT = 400, 600
GRID_SIZE = 40
GRID_ROWS = HEIGHT // GRID_SIZE
GRID_COLS = WIDTH // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player vs Bot Car Racing")
clock = pygame.time.Clock()

# === Colors ===
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
LIGHT_GREEN = (0, 255, 0)

# === Constants ===
CAR_WIDTH, CAR_HEIGHT = 40, 70
FINISH_LINE_Y = 50
font = pygame.font.SysFont(None, 40)

# === Load Images ===
ASSET_DIR = os.path.join(os.path.dirname(__file__), "assets")
player_car_img = pygame.image.load(os.path.join(ASSET_DIR, "player_car.webp"))
bot_car_img = pygame.image.load(os.path.join(ASSET_DIR, "bot_car.webp"))

player_car_img = pygame.transform.scale(player_car_img, (CAR_WIDTH, CAR_HEIGHT))
bot_car_img = pygame.transform.scale(bot_car_img, (CAR_WIDTH, CAR_HEIGHT))

# === A* Pathfinding Function ===
def a_star(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}

    def h(pos):
        return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])  # Manhattan distance

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        x, y = current
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
        for nx, ny in neighbors:
            if 0 <= nx < GRID_COLS and 0 <= ny < GRID_ROWS:
                neighbor = (nx, ny)
                temp_g = g_score[current] + 1
                if neighbor not in g_score or temp_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = temp_g
                    f = temp_g + h(neighbor)
                    heapq.heappush(open_set, (f, neighbor))
    return []

# === Game Function ===
def run_game():
    player_x = WIDTH // 4
    bot_x = WIDTH * 3 // 4
    player_y = HEIGHT - CAR_HEIGHT - 10
    bot_y = HEIGHT - CAR_HEIGHT - 10
    player_speed = 4
    bot_speed = 4
    winner = None
    running = True

    while running:
        screen.fill(GRAY)

        # Draw finish line
        pygame.draw.line(screen, YELLOW, (0, FINISH_LINE_Y), (WIDTH, FINISH_LINE_Y), 5)

        # Road lines
        for i in range(0, HEIGHT, 40):
            pygame.draw.rect(screen, WHITE, (WIDTH//2 - 5, i, 10, 20))

        # Rectangles for collision detection
        player_rect = pygame.Rect(player_x, player_y, CAR_WIDTH, CAR_HEIGHT)
        bot_rect = pygame.Rect(bot_x, bot_y, CAR_WIDTH, CAR_HEIGHT)

        # Draw cars
        screen.blit(player_car_img, (player_x, player_y))
        screen.blit(bot_car_img, (bot_x, bot_y))

        # === BOT AI: A* Path Planning ===
        bot_grid_x = bot_x // GRID_SIZE
        bot_grid_y = bot_y // GRID_SIZE
        player_grid_x = player_x // GRID_SIZE
        finish_grid_y = FINISH_LINE_Y // GRID_SIZE

        path = a_star((bot_grid_x, bot_grid_y), (player_grid_x, finish_grid_y))
        if path:
            next_x, next_y = path[0]
            target_px = next_x * GRID_SIZE
            target_py = next_y * GRID_SIZE

            if bot_x < target_px:
                bot_x += bot_speed
            elif bot_x > target_px:
                bot_x -= bot_speed
            if bot_y > target_py:
                bot_y -= bot_speed

        # Player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - CAR_WIDTH:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < HEIGHT - CAR_HEIGHT:
            player_y += player_speed

        # Check finish line
        if player_y <= FINISH_LINE_Y and bot_y <= FINISH_LINE_Y:
            winner = "It's a Tie!"
            running = False
        elif player_y <= FINISH_LINE_Y:
            winner = "You Win!"
            running = False
        elif bot_y <= FINISH_LINE_Y:
            winner = "Bot Wins!"
            running = False

        # Collision check
        if player_rect.colliderect(bot_rect):
            winner = "Crash! Bot Wins!"
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
        clock.tick(60)

    # Show result
    screen.fill(WHITE)
    text = font.render(winner, True, BLACK)
    screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
    pygame.display.flip()
    pygame.time.wait(3000)

# === Start Screen ===
def draw_start_screen():
    screen.fill(WHITE)
    title = font.render("Car Racing Game", True, BLACK)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//4))

    button_rect = pygame.Rect(WIDTH//2 - 75, HEIGHT//2, 150, 50)
    pygame.draw.rect(screen, LIGHT_GREEN, button_rect)
    start_text = font.render("Start Game", True, BLACK)
    screen.blit(start_text, (button_rect.centerx - start_text.get_width()//2,
                             button_rect.centery - start_text.get_height()//2))
    pygame.display.flip()
    return button_rect

# === Main Menu Loop ===
def main():
    while True:
        button_rect = draw_start_screen()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        waiting = False
                        run_game()

main()
