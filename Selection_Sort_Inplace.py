def selection(input):
    l = len(input)
    if l>1:
        n = l-1
        while n:
            max_val = max(input[:n+1])
            index = input.index(max_val)
            temp=input[n]
            input[n]=max_val
            input[index] = temp
            n-=1
    return input
