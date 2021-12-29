s = int(input())

a = set()
a.add(s)

ai = s


def f(n):
    if n % 2 == 0:
        return n//2
    else:
        return 3*n+1


for i in range(2, 1000000):
    ai = f(ai)
    if ai in a:
        print(i)
        break
    else:
        a.add(ai)
