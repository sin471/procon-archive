import cmath
import math

a, b = map(int, input().split())

z = complex(a, b)

rad = cmath.phase(z)

print(math.cos(rad), math.sin(rad))
