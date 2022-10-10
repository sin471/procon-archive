from math import factorial


def comb(n, r):
    permutations = 1
    for i in range(r):
        permutations *= n - i

    return permutations // factorial(r)


n = int(input())
a = list(map(int, input().split()))

balls = dict()

for a_i in a:
    balls.setdefault(a_i, 0)
    balls[a_i] += 1

balls_comb_sum = sum(comb(value, 2) for value in balls.values())

for a_i in a:
    print(balls_comb_sum - comb(balls[a_i], 2) + comb(balls[a_i] - 1, 2))
