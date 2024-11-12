def count_even(lst):
    """
    Returns the number of even numbers in the list lst.
    >>> count_even([1, 2, 3, 4])
    2
    >>> count_even([1, 3, 5, 7])
    0
    """
    count = 0  
    for num in lst: 
        if num % 2 == 0:  
            count += 1  

    print(count) 

def get_list_of_ints():
    """
    Reads in integers from the user until they press enter without providing a number.
    Returns the list of integers entered by the user.
    """
    lst = []  
    user_input = input("Enter an integer or press enter to stop: ")  
    while user_input != "": 
        lst.append(int(user_input))  
        user_input = input("Enter an integer or press enter to stop: ") 

    return lst 

def main():
    lst = get_list_of_ints()  
    count_even(lst)  

if __name__ == '__main__':
    main()
