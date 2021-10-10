import operator

n, m = map(int, input().split())
a = [list(input()) for i in range(2*n)]
rank_list = list(range(1, 2*n+1))
for item, num in zip(a, range(1, 2*n+1)):
    item.append(0)
    item.append(num)


def zyanken(a, k, round_):
    x = a[k][round_]
    y = a[k+1][round_]

    if x == y:
        pass
    elif x == "G" and y == "C":
        a[k][-2] += 1
    elif x == "G" and y == "P":
        a[k+1][-2] += 1
    elif x == "P" and y == "C":
        a[k+1][-2] += 1
    elif x == "C" and y == "G":
        a[k+1][-2] += 1
    elif x == "P" and y == "G":
        a[k][-2] += 1
    elif x == "C" and y == "P":
        a[k][-2] += 1
    return


# a[-1]=人
# a[-2]=win数
for round_ in range(m):
    for k in range(0, 2*n, 2):
        zyanken(a, k, round_)

    a.sort(key=operator.itemgetter(-1))
    a.sort(key=operator.itemgetter(-2), reverse=True)

for i in range(2*n):
    print(a[i][-1])
