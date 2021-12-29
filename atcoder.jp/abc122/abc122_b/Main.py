s = input()

length = 0
ans = 0
for i in s:
    if i in ["A", "C", "G", "T"]:
        length += 1
    else:
        length = 0
    ans = max(ans, length)

print(ans)