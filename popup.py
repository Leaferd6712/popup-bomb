import tkinter as tk
import random

root = tk.Tk()
root.withdraw()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

popups = []

class MovingPopup:
    def __init__(self, number):
        self.window = tk.Toplevel()
        self.window.title("Popup")

        self.width = 200
        self.height = 100

        self.x = random.randint(0, screen_width - self.width)
        self.y = random.randint(0, screen_height - self.height)

        self.dx = random.choice([-5, 5])
        self.dy = random.choice([-5, 5])

        self.window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        label = tk.Label(self.window, text=f"Popup #{number}")
        label.pack(expand=True)

        button = tk.Button(self.window, text="Close", command=self.window.destroy)
        button.pack()

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x >= screen_width - self.width:
            self.dx *= -1

        if self.y <= 0 or self.y >= screen_height - self.height:
            self.dy *= -1

        self.window.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.window.after(30, self.move)


# create all popups first
for i in range(1000):
    popups.append(MovingPopup(i + 1))

# start movement AFTER all are created
def start_movement():
    for p in popups:
        p.move()

root.after(1000, start_movement)  # wait 1 second

root.mainloop()