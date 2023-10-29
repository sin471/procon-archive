from itertools import permutations

n = int(input())
r = input()
c = input()


def head(s):
    l = []
    for si in s:
        for sij in si:
            if sij != ".":
                l.append(sij)
                break
    return l


p = list(permutations(range(n)))
for a_indexes in p:
    for b_indexes in p:
        for c_indexes in p:
            if any(
                a_index == b_index or b_index == c_index or c_index == a_index
                for a_index, b_index, c_index in zip(a_indexes, b_indexes, c_indexes)
            ):
                continue

            s = [["."] * n for _ in range(n)]
            for i, a_index in enumerate(a_indexes):
                s[i][a_index] = "A"
            for j, b_index in enumerate(b_indexes):
                s[j][b_index] = "B"
            for k, c_index in enumerate(c_indexes):
                s[k][c_index] = "C"

            if "".join(head(s)) == r and "".join(head(zip(*s))) == c:
                print("Yes")
                print("\n".join("".join(si) for si in s))
                exit()
print("No")
