n, a, b = map(int, input().split())
s = input()

border = a+b
overseas_rank = 0
ranked_cnt = 0

for char in s:
    if char == "a":
        if ranked_cnt < border:
            ranked_cnt += 1
            print("Yes")
        else:
            print("No")
    elif char == "b":
        overseas_rank += 1
        if ranked_cnt < border and overseas_rank <= b:
            ranked_cnt += 1
            print("Yes")
        else:
            print("No")
    else:
        print("No")
