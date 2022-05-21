from string import ascii_lowercase, ascii_uppercase

s=input()

low=False
up=False
for i in s:
    if i in ascii_lowercase:
        low=True
    elif i in ascii_uppercase:
        up=True


print("Yes" if low and up and len(set(s))==len(s) else "No")
