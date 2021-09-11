#Python Program to Calculate the Number of Upper Case Letters
#and Lower Case Letters in a String
s = raw_input("Enter string:")
count1 = 0
count2 = 0
for i in s:
      if(i.islower()):
            count1 += 1
      elif(i.isupper()):
            count2 += 1
print("The number of lowercase characters is:",count1)
print("The number of uppercase characters is:",count2)
