numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers)
print(numbers[3])
print(numbers[3:8])
print(numbers * 2)

numbers[5] = 'intruder'
print(numbers)

for i in numbers:
    print(f'The number is' + i)
