s = {k: list(input()) for k in "abc"}
t = "a"
while len(s[t]):
    t = s[t].pop(0)
print(t.upper())