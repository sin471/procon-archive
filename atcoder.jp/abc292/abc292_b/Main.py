n, q = map(int, input().split())
events = [list(map(int, input().split())) for _ in range(q)]

cards = [0] * (n + 1)

for c, x in events:
    if c == 1:
        cards[x] += 1
    if c == 2:
        cards[x] += 2
    if c == 3:
        print("Yes" if cards[x] >= 2 else "No")
