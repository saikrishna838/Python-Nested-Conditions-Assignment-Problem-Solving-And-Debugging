n = int(input())
result1 = ((n % 5) == 0)
result2 = ((n % 7) == 0) 
result3 = n < 7
result = (result1 and result2) or result3
if result:
    print(n)
else:
    print(n % 5)
    print(n % 7)