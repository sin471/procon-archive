import io
import sys

_INPUT = """50 70 11
0 0
35 0
49 14
8 49
0 2
1 19
41 31
30 18
3 8
44 10
32 42
27 27
0 27
17 3
28 18
17 48
4 13
1 21
17 17
10 25
14 16
35 36
19 7
25 12
6 46
25 24
18 32
31 47
15 12
41 15
24 16
49 22
49 17
29 42
30 32
22 8
36 39
9 12
7 7
20 46
16 15
17 34
16 21
17 28
46 4
26 21
45 17
10 32
26 35
45 31
40 45
28 45
0 20
17 22
45 9
33 34
39 20
46 20
30 5
10 48
9 37
26 37
29 30
29 46
41 19
0 4
4 47
6 37
36 2
2 25
1 1 1
#
7 4 2
####
#...
#...
###.
#...
#...
#...
4 5 2
#...#
#...#
#...#
#####
8 3 2
###
.#.
.#.
.#.
.#.
.#.
.#.
.#.
4 5 2
####.
#..##
####.
#..##
5 4 2
####
#...
###.
#...
####
4 4 2
####
#..#
#..#
####
5 8 3
#......#
#......#
########
#......#
#......#
8 7 3
..###..
.##.##.
##...##
#.....#
#######
#.....#
#.....#
#.....#
8 8 3
..######
.##.....
##......
#.......
#.......
##......
.##.....
..######
9 6 3
#....#
#...##
#..##.
#.##..
###...
#.##..
#..##.
#...##
#....#
"""

sys.stdin = io.StringIO(_INPUT)

from sys import stdin
import pprint
N,K,B=map(int,stdin.readline().rstrip().split())
coords=[stdin.readline().rstrip().split() for _ in range(K)]
#polyominos=stdin.readlines()
_=input()
polyomino1=input()
_=stdin.readlines()
# pprint.pprint(N)
# pprint.pprint(K)
# pprint.pprint(B)
# pprint.pprint(coords)
# pprint.pprint(polyomino1)
print(N**2)
for i in range(N):
    for j in range(N):
        print(1,i,j)
