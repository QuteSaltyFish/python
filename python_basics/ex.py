x1 = 10
x2 = 20
numbers = []
for number in range(1, x2, 2):
    print(number)
    tmp = number ** 2
    numbers.append(tmp)
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
square = [x**2 for x in range(1, 10)]
print(square[-3:])
