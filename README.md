# Snakes With Desparate Game

This is a simple game called "Snakes With Desparate" developed by Harsh Gupta (Desparete Enuf) using the Pygame library. The game is a classic implementation of the popular Snake game, where the player controls a snake to eat food and grow longer while avoiding collision with the boundaries or itself.

## How to Play

1. Use arrow keys (UP, DOWN, LEFT, RIGHT) to move the snake in the respective directions.
2. The snake will grow longer by eating the red food blocks that appear randomly on the screen.
3. The game ends if the snake collides with the boundaries of the window or with itself.
4. Press the SPACE BAR to start the game and ENTER to continue after game over.

## Concepts Used

1. **Pygame Library**: Pygame is a Python library used for game development and multimedia applications. It provides various modules for handling graphics, sounds, events, and more. In this game, Pygame is used for window creation, event handling, and rendering graphics.

2. **Game Loop**: The game loop is a fundamental concept in game development. It continuously runs the game logic, processes player inputs, and renders the graphics until the game is exited.

3. **Collision Detection**: The code uses simple collision detection to check if the snake collides with the food or itself.

4. **Random Number Generation**: The game generates random positions for the food blocks using the `random` module.

5. **File Handling**: The game stores and retrieves the high score in the `Highscore.txt` file using file handling.

6. **Sound Effects**: The game uses sound effects for background music and game over events.

## Colors

The game uses various colors for different elements:
- `dirt_white`: Background color
- `egg_pulm`: Color for text and game over message
- `yellow`: Color for the welcome screen
- `red`: Color of the food block
- `green`: Color of the snake

## How to Start

To play the game, run the Python script in a Python environment with the required dependencies installed. Make sure you have the Pygame library installed.

## Acknowledgments

The "Snakes With Desparate" game was developed by Harsh Gupta (Desparete Enuf) as a fun and educational project. The game demonstrates basic game development concepts using the Pygame library. The code is provided here for reference and learning purposes.

## License

This project is open-source and licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code, but please provide proper attribution to the original creator, Harsh Gupta (Desparete Enuf).
