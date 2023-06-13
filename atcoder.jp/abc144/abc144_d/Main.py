from math import atan, degrees

a, b, x = map(int, input().split())
# b*a*(b/2tanθ) =x
# a*b^2=2xtanθ
# a*b^2/2x=tanθ

# b*a^2-(a^3tanθ)/2=x
# (b*a^2-x)=(a^3tanθ)/2
# ((b*a^2-x)*2)/a^3=tanθ
theta1 = atan((a * (b**2)) / (2 * x))
theta2 = atan((b * (a**2) - x) * 2 / (a**3))

if theta1 >= atan(b / a):
    print(degrees(theta1))
else:
    print(degrees(theta2))
