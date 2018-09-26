a = [1,3,5,6]
b = 2
if b in a:
    print(a.index(b))
else:
    for i in range(len(a)):
        if a[i] < b < a[i+1]:
            print(i+1)