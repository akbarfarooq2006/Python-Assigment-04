MAX_LENGTH = 3
lst = [1, 2, 3,4,5,6,7,8,9,10,11,12,13,14]
remove_item=[]
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        res=lst.pop()
        remove_item.append(res)
    if remove_item !=[] :
        for i in remove_item:
            print(f"Removed item is {i}")
    else :
        print("List is short enough {}".format(lst))
        
    

if __name__ == "__main__":
    shorten(lst)