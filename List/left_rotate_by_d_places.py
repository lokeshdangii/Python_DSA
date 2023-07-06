def rotateByOne(list1,d):
    n = len(list1)
    
    for a in range(d):
        first = list1[0]
        for i in range(n-1):
            list1[i] = list1[i+1]

        list1[n-1] = first

    return list1


l1 = [2,4,6,8,10]
l2 = [2,4,6,8,10,12,15,16,17,19,22,24]
d = 4
print(rotateByOne(l2,d))

# Direct Method

list = [10,20,30,40,50]
e = 2
list = list[e:] + list[:e]
print(list)
