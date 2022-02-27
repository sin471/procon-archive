n = int(input())
s = input()


l = s.split("C")
l = ["".join(sorted(i)) for i in l]


print("C".join(l).replace("BB","A"))
