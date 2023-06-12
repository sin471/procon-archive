x = int(input())
b, r = divmod(x, 11)
print(b * 2 + (r + 6 - 1) // 6)
