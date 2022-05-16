import math
x, y = [int(x) for x in input().split()]
while (x < 1 or x >= y or y > 10000):
    x, y = [int(x) for x in input().split()]
else:
    x = y - x
    x = math.ceil(y/x)
    print(x)
    
