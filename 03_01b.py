from collections import namedtuple

def can_we_take_the_order(driver, value):
    # if driver.index(2) > value:
    #     return True
    # return False
    return driver.car_capacity >= value

def main():
    #add code here
    # #create a driver with a name, car type, and car capacity
    # #an example you can use to practice: "Iris", "Toyota Prius", 7
    # driver = namedtuple("Iris", "Toyota Prius", 7)
    
    # #check if they can take a certain order, given their car's capacity.
    # print(can_we_take_the_order(driver, 3))
    # print(can_we_take_the_order(driver, 13))

    Driver = namedtuple("driverrrrrr", ["name", "car_type", "car_capacity"])
    iris = Driver("Iris", "Prius", 7)
    mat = Driver("Mat", "SUV", 27)
    sam = Driver("Sam", "bike", 1)
    print(can_we_take_the_order(iris, 2))
    print(can_we_take_the_order(iris, 20))
    return

if __name__ == "__main__":
    main()