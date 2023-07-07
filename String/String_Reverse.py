
def reverse(s):
    rev = ""
    for i in s:
        rev = i + rev 


    return rev



s = input("Enter a String :")
print(reverse(s))



# Direct Method

print(s[::-1])