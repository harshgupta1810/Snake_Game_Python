import pygame
import random
import os


pygame.init()
pygame.mixer.init()


# Colors
dirt_white = (219, 219, 215)
egg_pulm = (97, 64, 81)
yellow = (251,236,93)
red = (255, 0, 0)
green = (85,107,47)
hex_blue = (106,90,205)

# Creating window
screen_width = 800
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background Image
bgimg = pygame.image.load("OIP.jfif")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()


# Game Title
pygame.display.set_caption("Snakes With Desparate")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome() :
    exit_game = False
    while not exit_game :
        gameWindow.fill(yellow)
        text_screen("Welcome To Snakes With Desparate", hex_blue, 50, 220)
        text_screen("Press SPACE BAR for play ", hex_blue, 100, 300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('background.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    # cheak if high score file exists or not
    if (not os.path.exists("Highscore.txt")):
        with open("Highscore.txt", "w") as f:
            f.write("0")
    with open("Highscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(50, screen_width / 2)
    food_y = random.randint(50, screen_height / 2)
    score = 0
    init_velocity = 3
    snake_size = 20
    fps = 60
    while not exit_game:
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill(dirt_white)
            text_screen("Game Over! Press Enter To Continue", egg_pulm, 50, 220)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_m :
                        score += 10

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score +=10
                food_x = random.randint(50, screen_width / 2)
                food_y = random.randint(50, screen_height / 2)
                snk_length +=5
                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(dirt_white)
            text_screen("Score: " + str(score) , egg_pulm, 10, 10)
            text_screen("Score: " + str(hiscore) , egg_pulm, 500, 10)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('last.mp3')
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
                game_over = True
                pygame.mixer.music.load('last.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
gameloop()