h1, h2, h3, w1, w2, w3 = map(int, input().split())
H = [h1, h2, h3]
W = [w1, w2, w3]


ans = 0

r = range(1, 30 + 1)


def is_correct(values):
    for i in range(3):
        if sum(values[i]) != H[i]:
            return False

    for i in range(3):
        tmp = 0
        for j in range(3):
            tmp += values[j][i]

            if values[j][i] <= 0:
                return False
                
        if tmp != W[i]:
            return False

    return True


for a in r:
    for b in r:
        for d in r:
            for e in r:
                c = H[0] - (a + b)
                f = H[1] - (d + e)
                g = W[0] - (a + d)
                h = W[1] - (b + e)
                i = W[2] - (c + f)

                if is_correct([[a, b, c], [d, e, f], [g, h, i]]):
                    ans += 1

print(ans)
