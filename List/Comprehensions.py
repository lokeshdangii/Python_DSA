l1 = [x for x in range(11) if x%2 == 0]
print(l1)

l2 = [x for x in range(11) if x%2 != 0]
print(l2)

l3 = [x for x in [10,24,3,55,32,1,8,2] if x < 10 ]
print(l3)

l3 = [x for x in [10,24,3,55,32,1,8,2] if x > 10 ]
print(l3)


s = "geeksforgeeks" 
s1 = [x for x in s if x in "aeiou"]
print(s1)

s2 = "geeks", "compiler", "assembler", "coureser"
s3 = [x for x in s2 if x.startswith("c")]
print(s3)

l4 = [ x*2 for x in range(8)]
print(l4)


lc = ["geeks", "for", "geeks", "gfg","ide"]
lc1 = [x.upper() for x in lc if x.startswith("g")]
print(lc1)

d = dict(zip(l1,l2))
print(d)