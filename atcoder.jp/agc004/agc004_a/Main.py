a, b, c = map(int, input().split())

v = a*b*c

ans = float("Inf")
for red in [a*b*(c//2), b*c*(a//2), c*a*(b//2)]:
    blue = v-red
    ans = min(ans, abs(red-blue))

print(ans)
