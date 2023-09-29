def linear_search(array,key):

    for index in range(len(array)):

        if array[index]==key:
            return index
    return -1


# Driver Code

print(linear_search([20,40,70,10,12,11,29,75,46],29))