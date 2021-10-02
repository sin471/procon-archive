import itertools
N=input()

N_list=list(N)
len_N=len(N)
comb_list=list(itertools.permutations(N_list))

maximum=0


for comb in comb_list:
    if len_N%2==1:
        half=len_N//2+1
    else:
        half=len_N//2
    a=int("".join(comb[:half]))
    b=int("".join(comb[half:]))
    ab=a*b
    if ab>maximum:
        maximum=ab

print(maximum)

