n = int(input())

ans_list = []

for i in range(120):
    if not n:
        break
    if n % 2 == 0:
        ans_list.append("B")
        n //= 2
    else:
        ans_list.append("A")
        n -= 1

print("".join(ans_list[::-1]))
