from turtle import Turtle, Screen, textinput, bgcolor, title
import random
import os

# List of available turtle shapes
TURTLE_SHAPES = [
    'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
]

# List of available colors
ALL_COLORS = [
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
    'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
    'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
    'chocolate', 'coral', 'cornflowerblue', 'cornsilk', 'crimson',
    'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 'darkgray',
    'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange',
    'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue',
    'darkslategray', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue',
    'dimgray', 'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen',
    'fuchsia', 'gainsboro', 'ghostwhite', 'gold', 'goldenrod',
    'gray', 'green', 'greenyellow', 'honeydew', 'hotpink',
    'indianred', 'indigo', 'ivory', 'khaki', 'lavender',
    'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue', 'lightcoral',
    'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightpink',
    'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightsteelblue',
    'lightyellow', 'lime', 'limegreen', 'linen', 'magenta',
    'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple',
    'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred',
    'midnightblue', 'mintcream', 'mistyrose', 'moccasin', 'navajowhite',
    'navy', 'oldlace', 'olive', 'olivedrab', 'orange',
    'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise',
    'palevioletred', 'papayawhip', 'peachpuff', 'peru', 'pink',
    'plum', 'powderblue', 'purple', 'red', 'rosybrown',
    'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen',
    'seashell', 'sienna', 'silver', 'skyblue', 'slateblue',
    'slategray', 'snow', 'springgreen', 'steelblue', 'tan',
    'teal', 'thistle', 'tomato', 'turquoise', 'violet',
    'wheat', 'white', 'whitesmoke', 'yellow', 'yellowgreen'
]

# Global variables for scores and health
score1 = 0
score2 = 0
health1 = 100
health2 = 100
level = 1
enemies = []  # List to hold enemy turtles
enemy_health_displays = []  # List to hold enemy health display turtles


def draw_triangle(player, distance):
    for _ in range(3):
        player.forward(distance)
        player.left(120)


def draw_square(player, distance):
    for _ in range(4):
        player.forward(distance)
        player.left(90)


def draw_circles(player, radius, times):
    for _ in range(times):
        player.circle(radius)
        player.left(360/times)


def draw_triangles(player, distance, times):
    for _ in range(times):
        draw_triangle(player, distance)
        player.left(360/times)


def draw_squares(player, distance, times):
    for _ in range(times):
        draw_square(player, distance)
        player.left(360/times)


def rand_clr_shp_thick(player):
    player.color(random.choice(ALL_COLORS))
    player.shape(random.choice(TURTLE_SHAPES))  # Fixed the variable name
    player.pensize(random.randint(5, 20))


def random_motion(player):
    times = random.randint(10, 100)
    for _ in range(times):
        angle = random.randint(0, 360)
        distance = random.randint(0, 200)
        direction = random.randint(0, 1)
        if direction == 0:
            direction = player.left(angle)
        else:
            direction = player.right(angle)
        player.forward(distance)


def go_without_drawing(player, x, y):
    player.penup()
    player.goto(x, y)
    player.pendown()


def clear():
    """Clear the console screen."""
    os.system('cls' if os.name ==
              'nt' else 'clear')  # Clear the console based on the operating system


def get_input(prompt):
    """Get input from the user through a text input dialog."""
    return textinput("Input", prompt)


def get_speed():
    """Prompt the user to choose a speed for the turtle."""
    while True:
        speed = get_input(
            "Choose your speed:\n[1]. Slowest\n[2]. Slow\n[3]. Normal\n[4]. Fast\n[5]. Fastest")
        try:
            speed = int(speed)
            if speed in range(1, 6):
                # Return the corresponding speed
                return ["slowest", "slow", "normal", "fast", "fastest"][speed - 1]
            else:
                continue
        except (ValueError, TypeError):
            continue


def get_color():
    """Prompt the user to choose a color for the turtle."""
    while True:
        # Get user input and normalize it
        color = get_input("Choose a color:").strip().lower()
        if color in ALL_COLORS:
            return color  # Return the chosen color
        else:
            continue


def next_level():
    """Increase the level and adjust game parameters."""
    global level
    level += 1
    # Adjust enemy count, speed, or other parameters as needed
    for _ in range(level):  # Increase the number of enemies with each level
        enemies.append(create_hostile_turtle())
    update_display()  # Update the display for the new level


def get_shape():
    """Prompt the user to choose a shape for the turtle."""
    while True:
        # Get user input and normalize it
        shape = get_input("Choose a shape:").strip().lower()
        if shape in TURTLE_SHAPES:
            return shape  # Return the chosen shape
        else:
            continue


def move_player(player, direction):
    """Move the specified player turtle in the given direction."""
    directions = {
        "up": 90,
        "down": 270,
        "left": 180,
        "right": 0
    }
    player.setheading(directions[direction])
    player.forward(10)


def create_player(color, shape):
    """Create a turtle player with the specified color and shape."""
    player = Turtle()  # Create a new turtle instance
    player.shape(shape)  # Set the shape of the turtle
    player.color(color)  # Set the color of the turtle
    player.penup()  # Ensure the player starts without drawing
    return player  # Return the created player turtle


def create_hostile_turtle():
    """Create a hostile turtle that moves randomly."""
    enemy = Turtle()
    enemy.shape(random.choice(TURTLE_SHAPES))
    enemy.color(random.choice(ALL_COLORS))
    enemy.penup()
    enemy.speed(0)  # Set to 0 for instant movement
    # Random starting position
    enemy.goto(random.randint(-200, 200), random.randint(-200, 200))
    enemy.health = 100  # Initialize enemy health
    enemy_health_display = create_health_display_turtle(
        enemy)  # Create health display for the enemy
    # Store the health display turtle
    enemy_health_displays.append(enemy_health_display)
    return enemy


def create_health_display_turtle(enemy):
    """Create a turtle to display the health of the enemy."""
    health_display = Turtle()
    health_display.hideturtle()
    health_display.penup()
    health_display.goto(enemy.xcor(), enemy.ycor() +
                        20)  # Position above the enemy
    return health_display


def update_display():
    """Update the health, scores, and level display on the screen."""
    global health_display
    health_display.clear()
    health_display.goto(-200, 200)
    health_display.write(
        f"Player 1 Health: {health1}  Score: {score1}  Level: {level}", align="left", font=("Arial", 14, "normal"))
    health_display.goto(0, 200)
    health_display.write(
        f"Player 2 Health: {health2}  Score: {score2}  Level: {level}", align="center", font=("Arial", 14, "normal"))

    for enemy, health_display in zip(enemies, enemy_health_displays):
        # Update position above the enemy
        health_display.goto(enemy.xcor(), enemy.ycor() + 20)
        health_display.clear()  # Clear previous health display
        health_display.write(
            f"Health: {enemy.health}", align="center", font=("Arial", 10, "normal"))


def enemy_behavior(enemy, player1, player2):
    """Make the enemy move towards the nearest player."""
    if player1.distance(enemy) < player2.distance(enemy):
        enemy.setheading(enemy.towards(player1))
    else:
        enemy.setheading(enemy.towards(player2))
    enemy.forward(2)  # Move the enemy forward


def shoot(player):
    """Create a projectile and move it forward."""
    projectile = Turtle()
    projectile.shape("circle")
    projectile.color("yellow")
    projectile.penup()
    projectile.goto(player.position())
    projectile.setheading(player.heading())

    # Move the projectile
    for _ in range(50):  # Adjust the range for projectile distance
        projectile.forward(10)
        # Check for collision with enemies
        for enemy in enemies:
            if projectile.distance(enemy) < 15:  # Collision threshold
                enemy.health -= 20  # Decrease enemy health
                projectile.hideturtle()  # Hide the projectile
                update_display()  # Update the display
                return  # Exit after hitting an enemy
    projectile.hideturtle()  # Hide the projectile if it goes off-screen


def check_collision(player, enemy):
    """Check for collision between player and enemy."""
    return player.distance(enemy) <= 15  # Collision threshold


def main():
    """Main function to set up the game and start the event loop."""
    global health1, health2, score1, score2, enemies, health_display

    window = Screen()  # Create a new screen for the game
    window.bgcolor("black")  # Set the background color of the window
    window.setup(width=500, height=500)  # Set the dimensions of the window
    title("Turtle Game")

    # Create health display
    health_display = Turtle()
    health_display.hideturtle()
    health_display.penup()
    health_display.goto(-200, 200)

    # Get player 1's color, shape, and speed
    color1 = get_color()  # Get color for player 1
    shape1 = get_shape()  # Get shape for player 1
    player1 = create_player(color1, shape1)  # Create player 1

    # Get player 2's color, shape, and speed
    color2 = get_color()  # Get color for player 2
    shape2 = get_shape()  # Get shape for player 2
    player2 = create_player(color2, shape2)  # Create player 2

    # Create enemies
    enemies = [create_hostile_turtle() for _ in range(5)]  # Create 5 enemies

    # Start listening for key events
    window.listen()
    window.onkey(lambda: move_player(player1, "up"), "w")
    window.onkey(lambda: move_player(player1, "down"), "s")
    window.onkey(lambda: move_player(player1, "left"), "a")
    window.onkey(lambda: move_player(player1, "right"), "d")
    # Space key for player 1 to shoot
    window.onkey(lambda: shoot(player1), "space")

    window.onkey(lambda: move_player(player2, "up"), "Up")
    window.onkey(lambda: move_player(player2, "down"), "Down")
    window.onkey(lambda: move_player(player2, "left"), "Left")
    window.onkey(lambda: move_player(player2, "right"), "Right")
    # Enter key for player 2 to shoot
    window.onkey(lambda: shoot(player2), "Return")

    # Main game loop
    while True:
        for enemy in enemies:
            # Move enemies towards the nearest player
            enemy_behavior(enemy, player1, player2)

            # Check for collisions with player 1
            if check_collision(player1, enemy):
                health1 -= 10  # Decrease health for player 1
                # Reset enemy position
                enemy.goto(random.randint(-200, 200),
                           random.randint(-200, 200))
                score1 += 1  # Increase score for player 1
                update_display()  # Update health display
                if health1 <= 0:
                    print("Player 1 has been defeated!")
                    window.bye()  # Close the window if player 1 is defeated

            # Check for collisions with player 2
            if check_collision(player2, enemy):
                health2 -= 10  # Decrease health for player 2
                # Reset enemy position
                enemy.goto(random.randint(-200, 200),
                           random.randint(-200, 200))
                score2 += 1  # Increase score for player 2
                update_display()  # Update health display
                if health2 <= 0:
                    print("Player 2 has been defeated!")
                    window.bye()  # Close the window if player 2 is defeated

        update_display()  # Update the display for health and scores
        window.update()  # Update the screen


if __name__ == "__main__":
    main()  # Run the main function to start the game
