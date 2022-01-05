n = int(input())
s = input()

x = 0
ans = 0
for i in s:
    x = x+1 if i == "I" else x-1
    ans = max(ans, x)

print(ans)
