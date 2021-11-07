from decimal import Decimal, ROUND_HALF_UP
x=Decimal(input())
print(x.quantize(Decimal("0"),ROUND_HALF_UP))