l1 = [10,20,30]
l2 = l1[:]


t1 = (10,20,30)
t2 = t1[:]
print(t2)


s1 = "geeks"
s2 = s1[:]

print(l1 in l2)
print(t2 in t1)
print(s1 in s2)

print()

print(l1 is l2)
print(t2 is t1)
print(s1 is s2)