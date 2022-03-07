import sys
color = ['black', 'brown', 'red','orange','yellow', 'green', 'blue', 'violet', 'grey', 'white']
input = sys.stdin.read().splitlines()
resist = (color.index(input[0])*10 + color.index(input[1])) * 10**color.index(input[2])
print(resist)