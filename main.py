import turtle  # Import the turtle module
from turtle import Turtle, Screen  # Import Turtle and Screen classes from the turtle module
import random  # Import the random module

is_race_on = False  # Initialize the race status as False

# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)  # Set the screen size to 500x400 pixels

# Get the user's bet on which turtle will win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

# Define the colors for the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Define the starting y-positions for the turtles
y_positions = [-70, -40, -10, 20, 50, 80]

# Create a list to hold all the turtle objects
all_turtles = []

# Create and position each turtle
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # Create a new turtle object
    new_turtle.color(colors[turtle_index])  # Set the turtle's color
    new_turtle.penup()  # Lift the pen to avoid drawing lines
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Position the turtle at the starting line
    all_turtles.append(new_turtle)  # Add the turtle to the list

# Start the race if the user has placed a bet
if user_bet:
    is_race_on = True

# Run the race
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:  # Check if the turtle has crossed the finish line
            is_race_on = False  # End the race
            winning_color = turtle.pencolor()  # Get the color of the winning turtle
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner.")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner.")

        # Move the turtle forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Close the screen when clicked
screen.exitonclick()
