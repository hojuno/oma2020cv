natural_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiple_of_two = [a for a in natural_numbers if a % 2 == 0]

print(multiple_of_two)

natural_numbers = [a for a in range(1, 100)]
square_of_multiple_of_three = [a*a for a in natural_numbers if a%3 == 0]

print(square_of_multiple_of_three)
