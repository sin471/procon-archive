a, b, c = map(int, input().split())
if a == b or (abs(a) == abs(b) and c % 2 == 0):
    print("=")
    exit()

if (a >= 0 and b >= 0) or c % 2 == 0:
    if abs(a) < abs(b):
        print("<")
    else:
        print(">")
    exit()

if c % 2 == 1:
    if a < b:
        print("<")
    else:
        print(">")
