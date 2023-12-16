s1, s2 = list(input())
t1, t2 = list(input())

x = abs(ord(s1) - ord(s2))
y = abs(ord(t1) - ord(t2))


print("Yes" if x + y == 5 or x == y else "No")
