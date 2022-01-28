from cgitb import reset


s = input()
a, b, c, d = s[0], s[1], s[2], s[3]

op = ["+", "-"]

k = 3


def calculate(exp):
    result = int(exp[0])
    for i in range(1, len(exp), 2):
        next_num = int(exp[i+1])
        if exp[i] == "+":
            result += next_num
        else:
            result -= next_num

    return result


for i in range(1 << k):
    l = []
    for bit in range(k):
        if (1 << bit) & i:
            l.append("+")
        else:
            l.append("-")

    exp = "".join([a, l[0], b, l[1], c, l[2], d])

    if calculate(exp) == 7:
        print(f"{exp}=7")
        exit()
