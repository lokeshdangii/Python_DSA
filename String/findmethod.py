s1 = "geeks for geeks"
s2 = "geeks"

print(s1.find(s2))
print(s1.find("gfg"))

n = len(s1)
print(s1.find(s2,1,n))

# Differnce between find and index method is that index method will give error if not found the string whereas find will give -1