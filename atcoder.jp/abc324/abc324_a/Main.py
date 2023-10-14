n = int(input())
a = list(map(int, input().split()))
print("Yes" if all(map(lambda x: a[0] == x, a)) else "No")
