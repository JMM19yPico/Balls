from Ball2D import Ball2D
import matplotlib.pyplot as plt


def main():
    ball = Ball2D(0, 0, 1, 'blue')  # Example: Create a ball at (0, 0) with radius 10
    print(f"Ball position: {ball.x}, {ball.y}")
    ax = ball.plot()  # Plot the ball
    ball.move(5, 5)  # Move the ball by (5, 5)
    ball.set_color('red')  # Change the color of the ball
    ax = ball.plot(ax)  # Plot the ball again to see the changes
    print(f"Ball position after moving: {ball.x}, {ball.y}")
    plt.show()  # Show the plot with the ball

    
if __name__ == "__main__":
    main()