import matplotlib.pyplot as plt

class Ball2D:
    def __init__(self, x=0, y=0, radius=1, color='red'):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def plot(self):
        fig=plt.figure()
        ax = fig.add_subplot(111)
        ax.set_title('Ball2D')
        circle = plt.Circle((self.x, self.y), self.radius, color=self.color)
        ax.add_artist(circle)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal', adjustable='box')
        plt.show()


    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def get_position(self):
        return self.x, self.y

    def get_radius(self):
        return self.radius
    
    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color

    def set_radius(self, radius):
        self.radius = radius

    def set_position(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Ball2D(x={self.x}, y={self.y}, radius={self.radius}, color={self.color})"