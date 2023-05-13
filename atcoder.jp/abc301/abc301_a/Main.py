n = int(input())
s = input()
cnt1 = cnt2 = 0
for i in range(n):
    if s[i] == "T":
        cnt1 += 1
    else:
        cnt2 += 1

    if cnt1 >= n / 2:
        print("T")
        break
    elif cnt2 >= n / 2:
        print("A")
        break
