from string import ascii_lowercase
n = int(input())
s = [input() for _ in range(n)]

l = [char * min(map(lambda s_i: s_i.count(char), s)) for char in ascii_lowercase]

print("".join(l))
