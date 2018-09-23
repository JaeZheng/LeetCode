import re
pattern = "^\-\d+|\d+"
a = "-0012a42"
if re.match(pattern, a) is not None:
    print(type(re.match(pattern, a).span()))
    start,end = re.match(pattern, a).span()
    print(a[start:end])
    print("True!!!")
else:
    print("False!!!")
