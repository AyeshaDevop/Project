def get_user_numbers():
    """
    Prompts the user to input numbers, storing them in a list. 
    Stops collecting input when a blank line is entered.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")

        if user_input == "":
            break
        
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid integer.")

    return user_numbers

def count_nums(num_lst):
    """
    Takes a list of numbers and counts occurrences of each number.
    Returns a dictionary with numbers as keys and counts as values.
    """
    num_dict = {}
    for num in num_lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    
    return num_dict

def print_counts(num_dict):
    """
    Prints each number and its count from the dictionary.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")

def main():
    """
    Collects numbers from the user, counts occurrences, and prints the results.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)

if __name__ == '__main__':
    main()
