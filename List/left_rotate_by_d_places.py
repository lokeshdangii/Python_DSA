def rotateByOne(list1):
    d = 2
    n = len(list1)
    
    for a in range(d):
        first = list1[0]
        for i in range(n-1):
            list1[i] = list1[i+1]

        list1[n-1] = first

    return list1


l1 = [2,4,6,8,10]
print(rotateByOne(l1))