from car import *
my_electric_car = ElectricCar('tesla', 'model s', 2016)
my_beetle = Car('volkswagen', 'bettle', 2016)
print(my_beetle.get_descriptive_name())
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
