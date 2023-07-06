# Invalid Syntax
'''
s = 'Welcome to Python's String'
print(s)
'''

# Corrected Program
s = 'Welcome to Python\'s String'  #this backslash makes python escape the single quote
print(s)

s1 = 'Hii\n welcome to the Python'
print(s1)

# '\n is ignored or escaped and is used for the new line'


s2 = "A simple \ example"
s3 = "Backslash at the end \\"
s4 = "\\n"
s5 = "\\t"

print(s2)
print(s3)
print(s4)
print(s5)
