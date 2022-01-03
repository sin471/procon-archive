n = int(input())
d, x = map(int, input().split())
a = [int(input()) for _ in range(n)]

l = [0]*(d+1)

for a_i in a:
    for k in range(d):
        eating_day = a_i*k+1
        if eating_day <= d:
            l[eating_day] += 1
        else:
            break

print(sum(l)+x)
