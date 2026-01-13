a = int(input())
b = int(input())
c = a % b
d = b % a
smallest_among = c > d
if smallest_among:
    print(d)
else:
    print(c)