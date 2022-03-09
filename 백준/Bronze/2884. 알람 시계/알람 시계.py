import sys
h, m = map(int, sys.stdin.readline().split()) 
if m < 45:
    if h > 0:
        print(h-1, 60-(45-m))
    else :
        print(23, 60-(45-m))
else:

        print(h, m-45)

