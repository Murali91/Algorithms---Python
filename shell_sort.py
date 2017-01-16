def shell(input):
    l = len(input)
    n = (l/2)
    while n>=1:
        r=l/n
        while r>0:
            for i in range(l-1,0,-n):
                if input[i]<input[i-n]:
                    temp = input[i-n]
                    input[i-n] = input[i]
                    input[i] = temp
            r-=1
        n=n/2
    return input
