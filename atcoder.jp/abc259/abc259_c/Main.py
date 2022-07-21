from itertools import groupby

s = input()
t = input()

compressed_s = [[char, len(list(iter_))] for char, iter_ in groupby(s)]
compressed_t = [[char, len(list(iter_))] for char, iter_ in groupby(t)]

def solve():
    if len(compressed_s) != len(compressed_t):
        return False

    for s_i, t_i in zip(compressed_s, compressed_t):
        is_same_char = s_i[0] == t_i[0]
        if not is_same_char:
            return False

        if (s_i[1] == t_i[1]) or (2 <= s_i[1] <= t_i[1]):
            continue
        else:
            return False

    return True


print("Yes" if solve() else "No")
