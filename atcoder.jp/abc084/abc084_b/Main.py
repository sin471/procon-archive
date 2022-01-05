a, b = map(int, input().split())
s = input()

ans = "No"
for i, si in enumerate(s):
    if i == a and si != "-":
        break

    if i != a and si not in "0123456789":
        break
else:
    ans = "Yes"
print(ans)
