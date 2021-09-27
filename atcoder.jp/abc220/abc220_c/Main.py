n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum_a = sum(a)
q = x//sum_a
y = sum_a*q
y_index = len(a)*q

for i, item in enumerate(a, 1):
    y += item
    if y > x:
        print(y_index+i)
        break
