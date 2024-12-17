import DrawingPanel
import random

panel = DrawingPanel.DrawingPanel(800, 600)

def backg():
    panel.fill_rect(0, 0, 800, 500, "light sky blue")  #sky
    panel.fill_oval(220, 380, 400, 400, "gold")       #sun
    panel.fill_rect(0, 500, 800, 600, "pale green")   #ground

def car(x, y):
    panel.fill_rect(x, y, 50, 15, "tomato")               #car body
    panel.fill_rect(x + 10, y - 10, 30, 10, "dark slate gray")  #car roof
    panel.fill_oval(x + 3, y + 7, 14, 14, "dim grey")     #left wheel
    panel.fill_oval(x + 30, y + 7, 14, 14, "dim grey")    #right wheel

def firework(x, y, size, color):
#drawing of firewokr
    for angle in range(0, 360, 15):  #lines every 15 degrees
        end_x = x + size * random.uniform(0.8, 1.2) * (random.choice([-1, 1]))
        end_y = y + size * random.uniform(0.8, 1.2) * (random.choice([-1, 1]))
        panel.draw_line(x, y, end_x, end_y, color)

#firework loop
for i in range(63):
    backg()
    car1_x = 60 + (i * 5)
    car2_x = 730 - (i * 5)

    car(car1_x, 479)
    car(car2_x, 479)

    #fireworks trigger when cars meet
    if car1_x + 50 >= car2_x:
        for f in range(10):  #10 fireworks bursts
            backg()
            car(car1_x, 479)
            car(car2_x, 479)
            firework(400, 300 - f * 20, 50, random.choice(["red", "yellow", "blue", "green", "purple"]))
            panel.sleep(100)
        break  #stop animation

    panel.sleep(70)

if i % 50 == 0:
    panel.clear(50)
