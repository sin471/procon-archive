n = int(input())
s = input()

if "ABC" not in s:
    print(-1)
    exit()
print(s.index("ABC")+1)
