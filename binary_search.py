def binary_search(array,start_element,end_element,element):
    
    while (start_element<=end_element):
        mid=start_element+((end_element-start_element))//2
        
        if array[mid]==element:
            return mid
        elif array[mid]<element:
            start_element=mid+1
        else:
            end_element=mid-1
                
    return -1 

array=[2,5,10,14,18,22,27,35,40,59]
print(binary_search(array,0,len(array)-1,14))


