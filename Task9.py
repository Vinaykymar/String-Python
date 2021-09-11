#Python Program to Count Number of Lowercase Characters in a String
s = raw_input("Enter string:")
count = 0
for i in s:
      if(i.islower()):
            count += 1
print("The number of lowercase characters is:",count)
