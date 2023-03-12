x1, y1, x2, y2 = map(int, input().split())

# (x,y)->(y,-x)
moved_x2 = moved_y2 = 0
moved_x1 = x1 - x2
moved_y1 = y1 - y2
x3, y3 = moved_y1 + x2, -moved_x1 + y2


# (x,y)->(-y,x)
moved_x1 = moved_y1 = 0
moved_x2 = x2 - x1
moved_y2 = y2 - y1
x4, y4 = -moved_y2 + x1, moved_x2 + y1

print(x3, y3, x4, y4)
