num = list(map(int, input().split()))
sum_ = []
for i in range(len(num)):
  sum_.append(num[i]**2)
print(sum(sum_)%10)