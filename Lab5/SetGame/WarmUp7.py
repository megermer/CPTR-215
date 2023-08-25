def is_list_mult10(my_list): return all([item % 10 == 0 for item in my_list])
def is_list_no_mult10(my_list): return all([item % 10 != 0 for item in my_list])
if __name__ == '__main__':
    myList = [int(input()) for i in range(int(input()))]
    print("all multiples of 10" if is_list_mult10(myList) else "no multiples of 10" if is_list_no_mult10(myList) else "mixed values")
         
