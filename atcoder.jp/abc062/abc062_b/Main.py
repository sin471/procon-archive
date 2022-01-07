h, w = map(int, input().split())
a = [input() for _ in range(h)]

a.insert(0, "#"*w)
a.append("#"*w)
for i in a:
    print(f"#{i}#")
    