n =  int(input())
n = str(n)
result = ((int(n[0]) ** 4) + (int(n[1]) ** 4) + (int(n[2]) ** 4) + (int(n[3]) ** 4) ) == int(n)
if result:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")