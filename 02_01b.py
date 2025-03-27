from collections import deque

def main():
    foods = deque(maxlen=5)
    foods.append("STA001") # STA001
    ordered_foods = ["DES","STA","ENT","ENT"] # STA001, "DES","STA","ENT","ENT"
    foods.extend(ordered_foods)
    foods.append("STA061")  # "DES","STA","ENT","ENT", STA061
    foods.append("STA062")  # "STA","ENT","ENT", STA061, STA062
    foods.appendleft("STA063")  # STA063, "STA","ENT","ENT", STA061
    print(foods)
    return

if __name__ == "__main__":
    main()