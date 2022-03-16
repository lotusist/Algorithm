N = list(map(int, input().split()))
ascending = list(range(1,9))
descending = list(range(8, 0, -1))
if N == ascending:
  print("ascending")
elif N == descending:
  print("descending")
else :
  print("mixed")