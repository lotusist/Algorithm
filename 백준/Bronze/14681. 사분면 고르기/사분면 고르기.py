import sys
x, y = map(int, sys.stdin.read().splitlines())
if y > 0:
    if x > 0:
        print(1)
    else :
        print(2)
else :
    if x < 0:
        print(3)
    else :
        print(4)

