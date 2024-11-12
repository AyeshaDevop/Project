def read_phone_numbers():
    """
    Collects names and phone numbers from the user and stores them in a dictionary.
    Returns the completed phonebook.
    """
    phonebook = {}  

    while True:
        name = input("Name: ")
        if name == "":  
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):
    """
    Prints each name and corresponding number in the phonebook.
    """
    for name, number in phonebook.items():
        print(f"{name} -> {number}")

def lookup_numbers(phonebook):
    """
    Allows the user to look up numbers by entering a name.
    Prints the corresponding number if the name is found; otherwise, indicates if the name isn't in the phonebook.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "": 
            break
        if name in phonebook:
            print(phonebook[name])  
        else:
            print(f"{name} is not in the phonebook") 

def main():
    phonebook = read_phone_numbers() 
    print("Phonebook Entries:")
    print_phonebook(phonebook)      
    lookup_numbers(phonebook)        

if __name__ == '__main__':
    main()
