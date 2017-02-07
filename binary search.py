def binary(arr,data):
    arr = sorted(arr)
    middle = len(arr)/2
    if middle >=1:
        if arr[middle]>data:
            binary(arr[:middle],data)
        elif arr[middle]<data:
            binary(arr[middle:],data)
        else:
            print True
    else:
        if arr and arr[0] == data:
            print True
        else:
            print False
