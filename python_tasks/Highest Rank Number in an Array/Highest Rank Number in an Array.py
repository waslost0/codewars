def highest_rank(arr):
    counter = 0
    num = arr[0] 
      
    for i in arr: 
        curr_frequency = arr.count(i)         
        if(curr_frequency> counter) or (curr_frequency >= counter and num < i): 
            counter = curr_frequency 
            num = i
            
    return num 