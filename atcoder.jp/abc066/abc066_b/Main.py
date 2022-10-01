s = input()


def odd_string(s):
    n = len(s)

    if n % 2 == 1:
        return 0

    m = n // 2
    if s[:m] == s[m:]:
        return n


for i in range(len(s)-1,-1,-1):
    x=odd_string(s[:i])
    if x:
        print(x)
        break
