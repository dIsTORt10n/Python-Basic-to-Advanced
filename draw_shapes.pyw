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
    player.pensize(random.randint(3, 10))


def go_without_drawing(player, x, y):
    player.penup()
    player.goto(x, y)
    player.pendown()


def clear():
    """Clear the console screen."""
    os.system('cls' if os.name ==
              'nt' else 'clear')  # Clear the console based on the operating system


def main():
    """Main function to set up the game and start the event loop."""
    window = Screen()  # Create a new screen for the game
    window.bgcolor("black")  # Set the background color of the window
    window.setup(width=1000, height=1000)  # Set the dimensions of the window
    title("Turtle Game")
    player = Turtle()
    # Main game loop
    while True:
        shape = window.textinput(
            "Please enter a shape", "What do you want to draw? circle, square, triangle.").strip().lower()
        if shape not in ["circle", "triangle", "square", "exit", "quit"]:
            window.textinput("ERROR", "Invalid input.")
            continue

        rand_clr_shp_thick(player)

        if shape == "circle":
            player.circle(random.randint(50, 200))
        elif shape == "triangle":
            draw_triangle(player, random.randint(50, 200))
        elif shape == "square":
            draw_square(player, random.randint(50, 200))
        else:
            window.clear()
            window.bgcolor("red")
            player.hideturtle()
            player.write("Click anywhere to exit", align="center",
            font=("arial", 40, "bold"))
            window.exitonclick()


if __name__ == "__main__":
    main()  # Run the main function to start the game
