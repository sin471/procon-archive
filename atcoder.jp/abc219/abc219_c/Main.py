import string

X = input()
N = int(input())
S = [input() for _ in range(N)]

alphabet = string.ascii_lowercase


def replace_S(S):
    key = str.maketrans(X, alphabet)
    s_char = "-".join(S)
    translated_s = s_char.translate(key)
    l = translated_s.split("-")
    return l


def recover(s):
    s_char = "-".join(s)
    key2 = str.maketrans(alphabet, X)
    ans_list = s_char.translate(key2).split("-")
    return ans_list


s_list = replace_S(S)

s_list.sort()

ans_list = recover(s_list)

for ans in ans_list:
    print(ans)
