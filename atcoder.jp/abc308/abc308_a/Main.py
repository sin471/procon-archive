s = list(map(int, input().split()))


def solve():
    if not (s[0] % 25 == 0 and 100 <= s[0] <= 625):
        return False
    
    for i in range(1, 8):
        if not s[i - 1] <= s[i]:
            return False
        if not 100 <= s[i] <= 675:
            return False
        if not s[i] % 25 == 0:
            return False
    return True


print("Yes" if solve() else "No")
