from collections import deque

def check_pali(pali):
    d = deque(pali)

    while len(d) != 0 and len(d) != 1:
        right = d.pop()
        left = d.popleft()
        if right != left:
            return False
    return True

def main():
    #add code here
    pali = "tacocat"
    print(check_pali(pali))

if __name__ == "__main__":
    main()