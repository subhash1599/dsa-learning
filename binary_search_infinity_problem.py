import math
def binary_search_inf(array,start_element,end_element,element):
    
    while (start_element<=end_element):
        mid=start_element+((end_element-start_element))//2
        
        if array[mid]!=math.inf:
            start_element=mid+1
        
        elif array[mid]==math.inf:
            if array[mid -1]!=math.inf:
                return mid
        else:
            end_element=mid-1

    return -1 

array=[20,-30,10,5,7,0,29,56,220,math.inf,45,8,math.inf]
print(binary_search_inf(array,0,len(array)-1,math.inf))


