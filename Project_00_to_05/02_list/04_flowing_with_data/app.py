def add_three_copies(lst, data):
    
    lst.append(data)
    lst.append(data)
    lst.append(data)


def main():
   
    my_list = []
    
    
    message = input("Enter a message to copy: ")
    
    # list before copying
    print("List before:", my_list)
    add_three_copies(my_list, message)
    # List after copying
    print("List after:", my_list)

if __name__ == "__main__":
    main()