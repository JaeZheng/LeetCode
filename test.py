a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(a)
for i in range(len(a)):
    a[i]="".join((lambda x:(x.sort(),x)[1])(list(a[i])))
print(a)
s = "eat"
s = "".join((lambda x:(x.sort(), x)[1])(list(s)))
print(s)