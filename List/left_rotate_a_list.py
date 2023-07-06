l = [10,20,30,40]
print(l[1:])
print(l[0:1])
l = l[1:] + l[0:1]
print(l)

# l = l + [80]
# print(l)


# Another Method that is pop append method

l2 = [2,4,6,8,10]
l2.append(l2.pop(0))
print(l2)