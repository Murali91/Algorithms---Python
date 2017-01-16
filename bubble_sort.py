def bubble(input):
    l = len(input)
    if l>1:
        n = l -1
        while n:
            for index in range(l-1):
                if input[index]>input[index+1]:
                    temp = input[index]
                    input[index] = input[index+1]
                    input[index+1] = temp
            n-=1
    return input
