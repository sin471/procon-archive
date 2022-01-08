n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

temperatures = list(map(lambda x: t-x*0.006, h))

x = float("INf")

for i, temperature in enumerate(temperatures,1):
    if x > abs(temperature-a):
        x = abs(temperature-a)
        ans = i

print(ans)
