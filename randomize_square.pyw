from turtle import Turtle, Screen
import random

# --- Constants & Configuration ---

# List of available shapes for the turtle cursor
TURRLE_SHAPES = [
    'arrow', 'turtle', 'circle', 'square', 'triangle',
    'classic', 'triangle', 'classic'
]

# Comprehensive list of CSS color names supported by Tkinter/Turtle
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

# --- Input Functions ---


def get_color():
    """Prompts the user for a color name until a string is provided."""
    while True:
        try:
            wanted_color = str(input("Choose a valid color: ")).strip().lower()
            break
        except TypeError:
            print("ERROR: Please enter a color name.")
            input("Press 'Enter' to continue.")
            continue
    return wanted_color


def get_shape():
    """Prompts the user for a shape name until a string is provided."""
    while True:
        try:
            wanted_shape = str(input("Choose a shape:")).strip().lower()
            break
        except TypeError:
            print("ERROR: Please enter a valid shape name.")
            input("Press 'Enter' to continue.")
            continue
    return wanted_shape

# --- Drawing Functions ---


def draw_triangle(player, distance):
    """Draws a single equilateral triangle."""
    for _ in range(3):
        player.forward(distance)
        player.left(120)


def draw_sqaure(player, distance):
    """Draws a single square."""
    for _ in range(4):
        player.forward(distance)
        player.left(90)


def draw_circles(player, times, radius):
    """Draws a spirograph pattern using circles."""
    for _ in range(times):
        player.circle(radius)
        player.left(360/times)


def draw_triangles(player, distance, times):
    """Draws a spirograph pattern using triangles."""
    for _ in range(times):
        draw_triangle(player, distance)
        player.left(360/times)


def draw_squares(player, distance, times):
    """Draws a spirograph pattern using squares."""
    for _ in range(times):
        draw_sqaure(player, distance)
        player.left(360/times)

# --- Utility Functions ---


def randomize_player(player):
    """Assigns a random color, shape, and pen thickness to the turtle."""
    player.color(random.choice(ALL_COLORS))
    player.shape(random.choice(TURRLE_SHAPES))
    player.pensize(random.randint(5, 15))


def random_motion(player):
    """Moves the turtle in random directions and distances (Random Walk)."""
    times = random.randint(10, 30)
    for _ in range(times):
        direction = random.randint(0, 1)  # 0 for left, 1 for right
        angle = random.randint(0, 360)
        distance = random.randint(0, 200)
        if direction == 0:
            player.left(angle)
        else:
            player.right(angle)
        player.forward(distance)


def go_without_drawing(player, x, y):
    """Moves the turtle to a specific (x, y) coordinate without leaving a trail."""
    player.penup()
    player.goto(x, y)
    player.pendown()

# --- Main Logic ---


def main():
    # Screen Setup
    window = Screen()
    window.bgcolor("black")
    window.setup(width=500, height=500)

    # Turtle Initialization
    player1 = Turtle()
    player1.shape("turtle")
    player1.color("red")
    player1.speed("fastest")

    # Apply random styles
    randomize_player(player1)

    # Draw pattern 1: Circles in the bottom-left
    go_without_drawing(player1, -300, -300)
    draw_circles(player1, 100, 10)

    # Draw pattern 2: Triangles in the top-right
    go_without_drawing(player1, 300, 300)
    draw_triangles(player1, 100, 10)

    # Draw pattern 3: Squares in the center
    go_without_drawing(player1, 0, 0)
    draw_squares(player1, 100, 10)

    # Keep window open until clicked
    window.exitonclick()


if __name__ == "__main__":
    main()
