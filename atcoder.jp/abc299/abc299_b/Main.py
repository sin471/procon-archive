n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))
if t not in c:
    t = c[0]

l = [[i, c_i, r_i] for i, (c_i, r_i) in enumerate(zip(c, r))]

filtered=filter(lambda x: x[1] == t, l)
print(max(filtered, key=lambda x: x[2])[0] + 1)
