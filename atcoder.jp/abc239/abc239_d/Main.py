a, b, c, d = map(int, input().split())

p = set()
for i in range(2, 10000+1):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        p.add(i)


def solve():
    for i in range(a, b+1):
        for j in range(i+c, i+d+1):
            if j in p:
                break
        else:
            return "Takahashi"

    return "Aoki"


print(solve())
