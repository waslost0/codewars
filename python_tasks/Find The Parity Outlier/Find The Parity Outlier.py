def find_outlier(integers):
    even = [i for i in integers if i%2==0]
    odd = [i for i in integers if i%2 is not 0]
    
    return odd[0] if len(even) > len(odd) else even[0]