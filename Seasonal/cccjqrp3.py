import sys

def main():
    input = sys.stdin.read().strip().split()
    print((int(input[0]) + int(input[1]) + int(input[2]))%42069900169420) #mod number not just add (Question trick)

if __name__ == "__main__":
    main()