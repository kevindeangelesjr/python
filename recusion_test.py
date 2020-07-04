#def printlist(list):
#    list_len = len(list)
#    print(list)
#    
#    if list_len == 1:
#        num = list[0]
#        print(num)
#    else:
#        sublist = list[1:]
#        printlist(sublist)

#mylist = [5]
#mylist = [1, 2, 3, 4]
#printlist(mylist)

def list_sum_recursive(input_list):
    # Base case
    if input_list == []:
        return 0

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        return head + list_sum_recursive(smaller_list)

#print(list_sum_recursive([1, 2, 3]))

def print_list(input_list):

    list_len = len(input_list)

    # Base case
    if list_len == 1:
        print(input_list[0])

    # Recursive case
    # Decompose the original problem into simpler instances of the same problem
    # by making use of the fact that the input is a recursive data structure
    # and can be deﬁned in terms of a smaller version of itself
    else:
        head = input_list[0]
        smaller_list = input_list[1:]
        print(print_list(smaller_list))

print(print_list([1, 2, 3]))