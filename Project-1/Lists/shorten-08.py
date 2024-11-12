MAX_LENGTH = 3

def shorten(lst):

    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop() 
        print(last_elem)  

def get_lst():
    """
    Prompts the user to enter elements for the list one by one.
    Stops when the user enters an empty string.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()  
    shorten(lst)    

if __name__ == '__main__':
    main()