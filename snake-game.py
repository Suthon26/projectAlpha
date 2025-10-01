# Snake Game ด้วย Tkinter
import tkinter as tk
import random

WIDTH = 400
HEIGHT = 400
SEG_SIZE = 20

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        self.direction = 'Right'
        self.snake = [(SEG_SIZE*2, SEG_SIZE*2), (SEG_SIZE, SEG_SIZE*2), (0, SEG_SIZE*2)]
        self.food = self.place_food()
        self.running = True
        self.root.bind('<Up>', self.go_up)
        self.root.bind('<Down>', self.go_down)
        self.root.bind('<Left>', self.go_left)
        self.root.bind('<Right>', self.go_right)
        self.game_loop()

    def place_food(self):
        while True:
            x = random.randint(0, (WIDTH-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
            y = random.randint(0, (HEIGHT-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
            if (x, y) not in self.snake:
                return (x, y)

    def go_up(self, event):
        if self.direction != 'Down':
            self.direction = 'Up'
    def go_down(self, event):
        if self.direction != 'Up':
            self.direction = 'Down'
    def go_left(self, event):
        if self.direction != 'Right':
            self.direction = 'Left'
    def go_right(self, event):
        if self.direction != 'Left':
            self.direction = 'Right'

    def game_loop(self):
        if not self.running:
            return
        self.move_snake()
        self.check_collisions()
        self.draw()
        self.root.after(100, self.game_loop)

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Up':
            new_head = (head_x, head_y - SEG_SIZE)
        elif self.direction == 'Down':
            new_head = (head_x, head_y + SEG_SIZE)
        elif self.direction == 'Left':
            new_head = (head_x - SEG_SIZE, head_y)
        elif self.direction == 'Right':
            new_head = (head_x + SEG_SIZE, head_y)
        self.snake = [new_head] + self.snake[:-1]
        if new_head == self.food:
            self.snake.append(self.snake[-1])
            self.food = self.place_food()

    def check_collisions(self):
        head_x, head_y = self.snake[0]
        # ชนขอบ
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            self.game_over()
        # ชนตัวเอง
        if (head_x, head_y) in self.snake[1:]:
            self.game_over()

    def draw(self):
        self.canvas.delete('all')
        # วาดงู
        for i, (x, y) in enumerate(self.snake):
            color = 'green' if i == 0 else '#00cc00'
            self.canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill=color)
        # วาดอาหาร
        fx, fy = self.food
        self.canvas.create_oval(fx, fy, fx+SEG_SIZE, fy+SEG_SIZE, fill='red')

    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", fill="white", font=("Arial", 32))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
