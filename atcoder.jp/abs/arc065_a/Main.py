s=input()
word=["eraser","erase","dreamer","dream"]
for i in word:
    s=s.replace(i,"")

if not s:
    print("YES")
else:
    print("NO")

