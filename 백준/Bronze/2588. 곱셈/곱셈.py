a, b = int(input()), int(input())
print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)