s=[input() for _ in range(8)]

for i in range(8):
    for j in range(8):
        if s[i][j]=="*":
            print(chr(97+j)+str(8-i))
            #chr(48)=0
            #chr(57)=9
            #chr(65)=A
            #ord("A")=65
            #chr(90)=Z
            #chr(97)=a
            #chr(122)=z
