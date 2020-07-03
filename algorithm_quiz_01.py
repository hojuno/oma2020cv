import math
a = 612
divisor = []
root = int(math.sqrt(a))

for i in range(1, root+1):
    if a%i == 0:
        divisor.append(i)
        divisor.append(a//i)

print(divisor)
