from collections import defaultdict

n, x, y = map(int, input().split())


jewelry = {"red": [0] * (n + 1), "blue": [0] * (n + 1)}
jewelry["red"][n] = 1
lv = n
color = "red"

while lv != 1:
    if color == "red":
        jewelry["red"][lv - 1] += jewelry["red"][lv]
        jewelry["blue"][lv] += jewelry["red"][lv] * x
        jewelry["red"][lv] = 0
    elif color == "blue":
        jewelry["red"][lv - 1] += jewelry["blue"][lv]
        jewelry["blue"][lv - 1] += jewelry["blue"][lv] * y
        jewelry["blue"][lv] = 0

    if color == "blue":
        lv -= 1
    color = "blue" if color == "red" else "red"

print(jewelry["blue"][1])
