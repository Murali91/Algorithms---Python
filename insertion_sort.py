def insertion(input):
    l = len(input)
    count = 0
    if l>1:
        n = l-1
        while n:
            count+=1
            i=count-1
            while i>=0:
                if input[i+1]<input[i]:
                    temp = input[i]
                    input[i] = input[i+1]
                    input[i+1] = temp
                i-=1    
            n-=1
    return input
