a, b, c = map(int, input().split())

"""
root(a)+root(b)<root(c)
a+b+2root(ab)<c
2root(ab)<c-a-b
4ab<(c-a-b)^2
"""

print("Yes" if 4 * a * b < (c - a - b) ** 2 and (c - a - b) >= 0 else "No")
