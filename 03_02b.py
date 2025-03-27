from collections import namedtuple
import csv

def main():
    #add code here
    #read data/Customer.csv
    with open("data/Customer.csv", "r") as f:
        reader = csv.reader(f)
        # Picks up the header and creates Person() tuple
        Person = namedtuple("Person", next(reader))
        for read in reader:
                person = Person(*read)
                print(person)

    return

if __name__ == "__main__":
    main()