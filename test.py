## zip()函数单个参数
list1 = [1, 2, 3, 4]
dicted = {k: v for (k,v) in zip(list1, range(len(list1)))}
print(dicted)