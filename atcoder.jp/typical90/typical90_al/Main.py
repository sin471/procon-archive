a, b = map(int, input().split())
if a < b:
    a, b = b, a


def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)


gcd_ = gcd(a, b)

if b // gcd_ <= 10**18 // a:
    ans = a * b // gcd_
else:
    ans = "Large"

print(ans)
