_input= list(input())
_list = ['0','1','2','3','4','5','6','7','8','9',"A", "B", "C", "D", "E", "F"]
num = []
for i in range(len(_input)):
   num.append(_list.index(_input[i])*(16**(len(_input)-1-i)))
print(sum(num))