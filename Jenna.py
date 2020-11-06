 
def print_name():
    print('Jenna')
    return

def multiply_numbers():
    a = 8435*9983663
    print(a)
    return

def area_square(side_length):
    x= side_length 
    area = x*x
    print(area)
    return


def numbers():
    for i in range(1,101):
        print(i)

    return

def passing_grade(percent):
    if percent >= 95:
        print("A")
    if percent >= 90:
        print("B")
    if percent >= 80:
        print("C")
    else:
        print("F")
    return

def mean_list():
    num = [0,1,2,3]
    x = sum(num)/len(num)
    print(x)
    return


class Car:
    
    def __init__(self, color, brand, year):
        self.color = color
        self.brand = brand
        self.year = year

    def get_color(self, color):
        return self.color

    def get_brand(self, brand):
        return self.brand 

    def get_year(self, year):
        return self.year 
        

def create_car():
    car = Car('red','Ford','2020')
    print(car.get_color('red'))
    car.get_brand('Ford')
    car.get_year('2020')
    
    return

def fibonacci(n=100):
    z = 1
    x = 1
    for i in range(n):
        y = x+z
        x=z
        z=y
        print(y)
    return


# To run your code, just call the function here for example
print_name()
multiply_numbers()
area_square(3)
numbers()
passing_grade(85)
mean_list()
create_car()
fibonacci()


