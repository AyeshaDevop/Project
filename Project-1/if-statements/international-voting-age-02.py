AYESHA_AGE = 16
FATIMA_AGE = 25
ZARA_AGE = 48
def main():

    user_age = int(input("How old are you? "))

    if user_age >= AYESHA_AGE:
        print("You can vote in Ayesha where the voting age is " + str(AYESHA_AGE) + ".")
    else:
        print("You cannot vote in Ayesha where the voting age is " + str(AYESHA_AGE) + ".")
    
    if user_age >= FATIMA_AGE:
        print("You can vote in fatima where the voting age is " + str(FATIMA_AGE) + ".")
    else:
        print("You cannot vote in fatima where the voting age is " + str(FATIMA_AGE) + ".")
    
    if user_age >= ZARA_AGE:
        print("You can vote in Zara where the voting age is " + str(ZARA_AGE) + ".")
    else:
        print("You cannot vote in Zara where the voting age is " + str(ZARA_AGE) + ".")

if __name__ == '__main__':
    main()
