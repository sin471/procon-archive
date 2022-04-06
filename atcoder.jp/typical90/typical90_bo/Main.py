n, k = map(int, input().split())

s = str(n)


def base_x_to_10(n, x):
    s = str(n)
    l = [int(s[-(j+1)])*(x**j) for j in range(len(s))]
    return sum(l)


def base_10_to_x(n, x):
    l = [] if n != 0 else ["0"]
    while n != 0:
        l.append(str(n % x))
        n //= x

    return int("".join(l)[::-1])


n_8 = n
for i in range(k):
    n_10 = base_x_to_10(n_8, 8)
    n_9 = base_10_to_x(n_10, 9)
    n_8 = int(str(n_9).replace("8", "5"))

print(n_8)
