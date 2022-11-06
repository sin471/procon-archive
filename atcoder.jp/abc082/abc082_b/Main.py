s = sorted(input())
t = sorted(input(), reverse=True)


def is_dict_order(s, t):
    length = min(len(s), len(t))
    for i in range(length):
        if s[i] == t[i]:
            continue

        return s[i] < t[i]

    return len(s) < len(t)


print("Yes" if is_dict_order(s, t) else "No")
