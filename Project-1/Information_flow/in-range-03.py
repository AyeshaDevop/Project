def main():
    n = int(input("Enter a number: "))
    low = int(input("Enter the low bound: "))
    high = int(input("Enter the high bound: "))
    
    print(in_range(n, low, high)) # type: ignore

if __name__ == '__main__':
    main()

