MINIMUM_HEIGHT = 50 

def main():
    while True:
        height_input = input("How tall are you? ")
        if not height_input: 
            break
        try:
            height = float(height_input) 
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number for height.")

if __name__ == '__main__':
    main()
