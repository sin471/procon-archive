from sys import stdin
readline = stdin.readline
n = int(input())
a = list(map(int, readline().split()))
b = list(map(int, readline().split()))

c = [-1]*n
c[0] = a[0]*b[0]
a_max=a[0]
for i in range(1, n):
    c[i] = c[i-1]
    if a[i]>a_max:
      a_max=a[i]
    c_i = a_max*b[i]
    if c_i > c[i]:
        c[i] = c_i

print(*c, sep="\n")

