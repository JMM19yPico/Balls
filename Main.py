from Ball2D import Ball2D

def main():
    ball = Ball2D(0, 0, 1, 'yellow')  # Example: Create a ball at (0, 0) with radius 10
    ball.plot()  # Plot the ball
    print(f"Ball position: {ball.x}, {ball.y}")
    ball.move(5, 5)  # Move the ball by (5, 5)
    ball.set_color('blue')  # Change the color of the ball
    ball.plot()  # Plot the ball again to see the changes
    print(f"Ball position after moving: {ball.x}, {ball.y}")

if __name__ == "__main__":
    main()