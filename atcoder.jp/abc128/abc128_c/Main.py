n, m = map(int, input().split())
s = [list(map(int, input().split()))[1:] for _ in range(m)]
p = list(map(int, input().split()))
cnt = 0


def is_on_all(bits):
    for i in range(m):
        s_bits_sum = sum(bits >> ((x - 1)) & 1 for x in s[i])
        if s_bits_sum % 2 != p[i]:
            return False
    return True


for bits in range(1 << n):
    if is_on_all(bits):
        cnt += 1
print(cnt)
