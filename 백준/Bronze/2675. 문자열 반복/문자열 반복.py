T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    ans = []
    for i in S:
        ans.append(i*R)
    print(''.join(ans))