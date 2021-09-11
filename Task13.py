#  Python Program to Form a New String Made of the First 2 and
# Last 2 characters From a Given String
s = raw_input("Enter string:")
count=0
for i in s:
      count += 1
new=s[0:2]+s[count-1:count]
print("Newly formed string is:",new)
