l = [10,20,30,40]
print(l[1:])
print(l[0:1])
l = l[1:] + l[0:1]
print(l)

# l = l + [80]
# print(l)


# Another Method that is pop append method
'''
l2 = [2,4,6,8,10]
l2.append(l2.pop(0))
print(l2)
'''



# Using own Logic


def rotateByOne(list1):
    n = len(list1)
    first = list1[0]

    for i in range(n-1):
        list1[i] = list1[i+1]

    list1[n-1] = first

    return list1


l1 = [2,4,6,8,10]
print(rotateByOne(l1))

