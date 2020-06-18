a = [123, 24, 52, 7, 49, 3, 5, 2, 85]

for value in a:
    if value % 2 == 0:
        print(f'{value} is an even number')
    else:
        print(f'{value} is an odd number')


for value in range(0, 100):
    print(f'Counting number {value}')

for index, value in enumerate(a):
    print(f'No.{index} is {value}')

for index in range(len(a)):
    print(f'No.{index} is {a[index]}')
