# Duplicate this file, then try to complete as much as you can. 

def print_name(name):
    print(name)

def multiply_numbers(a, b):
    return a*b

def area_square(side_length):
    area = side_length**2
    return area


def numbers(a, b):
    for i in range(a, b+1):
        print(i)

def passing_grade(percent):
    if percent <= 100 and percent > 95:
        grade = 'A'
    elif percent <= 95 and percent > 90:
        grade = 'B'
    elif percent <= 90 and percent > 80:
        grade = 'C'
    else:
        grade = 'F'
    return grade

def mean_list(numlist):
    mean = 0
    nums = 0
    for i in numlist:
        mean += i
        nums += 1
    mean /= nums
    return mean



# Put the car class here
class Car:
    def __init__(self, color, brand, year):
        self.color = color
        self.brand = brand
        self.year = year

    def get_color(self):
        return self.color

    def set_color(self, x):
        self.color = x

    def get_brand(self):
        return self.brand

    def set_brand(self, x):
        self.brand = x

    def get_year(self):
        return self.year

    def set_year(self, x):
        self.year = x

def create_car():
    my_car = Car("red", "Ford", 2020)

    my_car.set_color("red")

    my_car.set_brand("Ford")

    my_car.set_year(2020)

    print(my_car.color)


def fibonacci(n=100):
    num = 1
    prevnum = 0
    tempnum = 0
    fibonacci_numbers = []
    while num < 100:
        fibonacci_numbers.append(num)
        tempnum = num
        num = num + prevnum
        prevnum = tempnum
    return fibonacci_numbers


# To run your code, just call the function here for example
print_name("Levi")

print(multiply_numbers(8435, 9983663))

print(area_square(3))

numbers(1, 100)

print(passing_grade(92))

create_car()

print(fibonacci())
