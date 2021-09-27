k = int(input())
a_b = input().split()

ab_10 = []

for item in a_b:
    digit = 0
    base_10 = 0
    for char in item[::-1]:
        base_10 += int(char)*(k**digit)
        digit += 1

    ab_10.append(base_10)

print(ab_10[0]*ab_10[1])
