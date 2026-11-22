import sys

def simple_interest(principal, intrest, time):
    return (principal * intrest * time) / 100

if __name__ == "__main__":
    if len(sys.argv) == 4:
        p = int(sys.argv[1])
        i = float(sys.argv[2])
        t = int(sys.argv[3])
    else:
        p = int(input("Enter Principal Amount: "))
        i = float(input("Enter Rate of Interest: "))
        t = int(input("Enter Time: "))

    print("Simple interest is:", simple_interest(p, i, t))