n = int(input())
s = input()

print(max(s.find(i) for i in "ABC")+1)
