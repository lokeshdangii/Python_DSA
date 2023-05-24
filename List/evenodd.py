def getEvenOdd(l):
    even = []
    odd = []

    for x in l:
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)

    return even,odd

list1 = [10,345,29,20,44,24,23,27,294]
print(getEvenOdd(list1))
even,odd = getEvenOdd(list1)
print(even)
print(odd)
