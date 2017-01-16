def merge_sort(input):
    middle = len(input)/2
    
    if middle>=1:
        left = input[:middle]
        right = input[middle:]
        merge_sort(left)
        merge_sort(right)
        i= 0
        j = 0
        k =0
        l = len(left)
        r = len(right)
        
        while i<l and j<r:
            if left[i]<right[j]:
                input[k] = left[i]
                i=i+1
            else:
                input[k] = right[j]
                j=j+1
            k+=1
            
        while i<l:
            input[k] = left[i]
            i+=1
            k+=1
        while j<r:
            input[k] = right[j]
            j+=1
            k+=1
    return input
