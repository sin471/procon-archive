from collections import Counter
from string import ascii_lowercase

s = input()
t = input()

s_counter = Counter(s)
t_counter = Counter(t)


def solve():
    for char in ascii_lowercase:
        if not (char in "atcoder@") and s_counter[char] != t_counter[char]:
            return False

    s_at = s_counter["@"]
    t_at = t_counter["@"]
    for char in "atcoder":
        cnt = s_counter[char] - t_counter[char]
        if cnt > 0:
            t_at -= cnt
        elif cnt < 0:
            s_at -= abs(cnt)

    if s_at < 0 or t_at < 0 or (s_at % 2 != t_at % 2):
        return False
    return True


print("Yes" if solve() else "No")
