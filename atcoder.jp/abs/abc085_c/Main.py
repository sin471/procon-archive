import sys
number_of_bill, sum_of_bill = map(int, input().split())

if number_of_bill*10000 < sum_of_bill or number_of_bill*1000 > sum_of_bill:
    print(-1, -1, -1)
    sys.exit()

for a in range(number_of_bill+1):
    for b in range(number_of_bill+1-a):
        c = number_of_bill-(a+b)

        if a*10000+b*5000+c*1000 == sum_of_bill:
            print(a, b, c)
            sys.exit()
        else:
            pass

else:
    print(-1, -1, -1)
