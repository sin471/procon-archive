h = int(input())
monster = 1
cnt = 0
while h > 0:
    h //= 2
    cnt += monster
    monster *= 2

print(cnt)