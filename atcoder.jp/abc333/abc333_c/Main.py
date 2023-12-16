n = int(input())

l = [int("1" * i) for i in range(1, 20)]

s = set()
for i in l:
    for j in l:
        for k in l:
            s.add(i + j + k)

print(sorted(s)[n - 1])