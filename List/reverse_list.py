# Reverse a list

def listReverse(l1):

    n = len(l1)
   
    for i in range(n//2):
        temp = l1[i]
        l1[i] = l1[n-1-i]
        l1[n-1-i] = temp

    return l1



list1 = ["Hii", "This", "is", "a", "python"]
list3 = [10,20,30,40]
list2 = [1,2,3,4,5,6,7,8,9,0]
rev = listReverse(list1)
print("The reverse of a list is : ",rev)


# list1.reverse()
# new_list = list1[::-1]
# print(new_list)