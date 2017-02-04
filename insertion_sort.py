def insertion(data):
    for i in range(1,len(data)):
        index = i
        value = data[i]
        while i>0 and data[i-1]>value:
            data[i] = data[i-1]
            i-=1
        data[i] = value
    print data
