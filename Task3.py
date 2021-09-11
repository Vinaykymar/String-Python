#>Python program to From a new String where the
#Fist Character and Last Character have been Exxchange
s = raw_input("Enter a string:")
fc = s[0]
lc = s[-1]
ms = s[1:len(s)-1]
ns = lc+ms+fc
print ns
