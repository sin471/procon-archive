m=int(input())
s_list=[input() for _ in range(m)]

key=str.maketrans("ACGT","TGCA")
for s in s_list:
    print(s.translate(key)[::-1])