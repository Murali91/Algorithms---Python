def quick_sort(input):
    n=0
    while n<len(input):
        i =1
        j = len(input)-1
        while i!=j:
            if input[i]<input[0]:
                i+=1
            if input[j]>input[0]:
                j-=1
            elif input[i]>input[0] and input[j]<input[0]:
                temp = input[j]
                input[j]=input[i]
                input[i]=temp
        if input[i]<input[0]:
            temp = input[0]
            input[0]=input[i]
            input[i]=temp
        else:
            temp = input[0]
            input[0]=input[i-1]
            input[i-1]=temp
        n+=1
    return input
