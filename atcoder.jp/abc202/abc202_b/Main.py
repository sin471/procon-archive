s=input()
s=s[::-1]
key=str.maketrans("69","96")
print(s.translate(key))