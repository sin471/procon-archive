n = int(input())
t = [int(input()) for _ in range(n)]


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


lcm = 1
for t_i in t:
    lcm = lcm * t_i // gcd(lcm, t_i)


print(lcm)
