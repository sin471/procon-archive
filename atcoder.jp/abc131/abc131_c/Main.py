from math import ceil

a, b, c, d = map(int, input().split())


def gcd(x, y):
    r = x % y

    if r == 0:
        return y

    return gcd(y, r)


lcm = (c*d)//gcd(c, d)


multiple_c_orless_b = b//c
multiple_d_orless_b = b//d
multiple_lcm_orless_b = b//lcm

multiple_c_or_d_orless_b = multiple_c_orless_b + \
    multiple_d_orless_b-multiple_lcm_orless_b

multiple_c_under_a = (a-1)//c
multiple_d_under_a = (a-1)//d
multiple_lcm_under_a = (a-1)//lcm

multiple_c_or_d_under_a = multiple_c_under_a + \
    multiple_d_under_a-multiple_lcm_under_a

print((b-a+1)-(multiple_c_or_d_orless_b-multiple_c_or_d_under_a))
