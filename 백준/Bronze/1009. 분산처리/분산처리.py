import sys

T = int(input())
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    c = a%10 # a를 10으로 나누었을 때 나머지
    if c == 0:
        print(10)
    elif c == 1 or c == 5 or c == 6:
        print(c)
    elif c == 4 or c == 9:
        if b % 2 == 1:
            print(c)
        else:
            print((c*c)%10)
    else:
        if b % 4 == 1:
            print(c)
        elif b % 4 == 2:
            print((c**2)%10)
        elif b % 4 == 3:
            print((c**3)%10)
        else:
            print((c**4)%10)
            
# what the time was over
# import sys
# T = int(input())
# for _ in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a**b%10 if a**b%10 != 0 else 10)
