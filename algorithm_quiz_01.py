a = 612
divisor = []
root = 100

for i in range(1, 101):
    if a%i == 0:
        divisor.append(i)
        divisor.append(a//i)

print(divisor)
