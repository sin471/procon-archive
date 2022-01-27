s = input()
k = int(input())

for i in range(len(s)):
    if s[i] != "1":
        print(s[i])
        break

    if k <= i+1:
        print(1)
        break
