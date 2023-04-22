n = int(input())
s = input()
flag = 0

for i in range(n):
    if s[i] == "|":
        flag += 1
        flag %= 2
    if flag and s[i] == "*":
        print("in")
        exit()

print("out")
