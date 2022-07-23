import cmath

a, b, d = map(int, input().split())

rad = cmath.pi * d / 180
z1 = a + (b * 1j)
z2 = cmath.cos(rad) + (cmath.sin(rad) * 1j)
z = z1 * z2
print(z.real, z.imag)
