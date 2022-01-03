n, a, b = map(int, input().split())

one_set = a+b
sets = n//one_set
blue = sets*a

remaining_balls = n % one_set

if remaining_balls >= a:
    blue += a
else:
    blue += remaining_balls
print(blue)
