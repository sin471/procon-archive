a, b, x = map(int, input().split())
b2 = b // x + 1

a2 = (a - 1) // x + 1 if a != 0 else 0

print(b2 - a2)
