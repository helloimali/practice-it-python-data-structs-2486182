from collections import namedtuple, defaultdict
import csv
from pprint import pprint

def main():
    # return 0 if the key does not exist
    dict = defaultdict(int)

    with open("data/OrderItems.csv", "r") as f:
        reader = csv.reader(f)
        OrderItem = namedtuple("OrderItem", next(reader))
        for line in reader:
            item = OrderItem(*line)
            dict[item.ProductID] = int(dict[item.ProductID])+ int(item.Quantity)
            # dict[item.ProductID] += int(item.Quantity)

    pprint(dict)
    return

if __name__ == "__main__":
    main()