a, b, c = map(int, input().split())

cnt = 0
is_even = a % 2 == b % 2 == c % 2 == 0
while is_even:
    a, b, c = (b + c) // 2, (a + c) // 2, (a + b) // 2
    
    is_equal = a == b or b == c or c == a
    is_even = a % 2 == b % 2 == c % 2 == 0
    cnt += 1

    if is_equal:
        print(-1)
        exit()

print(cnt)
