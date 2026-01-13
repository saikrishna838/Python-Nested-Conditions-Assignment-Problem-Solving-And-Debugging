n = int(input())
a = (n % 2) != 0 
b = n % 3 != 0
c = n % 5 != 0
d = n % 7 != 0
result = a and b and c and d
if result:
    print("True")
else:
    print("False")