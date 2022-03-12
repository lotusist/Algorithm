import sys
list_ = list(map(int, sys.stdin.read().splitlines()))
print(max(list_))
print(list_.index(max(list_))+1)