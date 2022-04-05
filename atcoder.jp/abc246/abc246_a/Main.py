from collections import Counter

x = []
y = []

for _ in range(3):
    x_i, y_i = list(map(int, input().split()))
    x.append(x_i)
    y.append(y_i)

print(Counter(x).most_common()[-1][0], Counter(y).most_common()[-1][0])
