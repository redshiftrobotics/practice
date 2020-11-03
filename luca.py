# Duplicate this file, then try to complete as much as you can. 
def print_name():
    # Your code here
    print("Luca")
    return

def multiply_numbers():
    # Your code here
    num = 8435 * 9983663
    print(num)
    return

def area_square(side_length):
    # Your code here
    area = side_length * side_length
    return area

def numbers():
    # Your code here
    for x in range(1,100):
        print(x)
    return

def passing_grade(score):
    # Your code here
    
    if score > 94:
        print("A")
    elif score > 89:
        print("B")
    elif score > 79:
        print("C")
    else:
        print("F")
    return 

testList = [3,4,5, 12]

def mean_list(list):
    # Your code here
    num = 0
    for x in list:
        num += x

    num = num / len(list)

    print(num)
    return 

# Put the car class here
class Car:

    def __init__(self, color, brand, year):
        self.color = color
        self.brand = brand
        self.year = year
        return

    def get_color(self):      
        return self.color

    def set_color(self, newCol):
        self.colr = newCol

def create_car():
    # Create a car here. Print color
    newCar = Car("red", "ford", 2020)
    print(newCar.get_color())
    return

def fibonacci(n=100):
    # Challenge one. Good luck
    print("Hello")
    return


# To run your code, just call the function here for example
create_car()