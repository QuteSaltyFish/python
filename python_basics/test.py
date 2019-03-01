name = "Wang Mingke"
age = 22
output = name + str(age)
bicycle = ['trek', 'canonale', 'redline']
message = "My bicycle is: " + bicycle[0].title() + '.'
print(message)
bicycle.append('evergrand')
bicycle.insert(0, 'bigmac')
print(bicycle)
del bicycle[0]
print(bicycle)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)

tmp = cars[:]
print(tmp)
tmp.pop()
print(tmp, cars)
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
