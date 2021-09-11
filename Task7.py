#Python Program to Calculate the Number of Words and the
#Number of Characters Present in a String
s=raw_input("Enter string:")
char=0
word=1
for i in s:
      char += 1
      if(i==' '):
            word += 1
print("Number of words in the string:")

print("Number of characters in the string:")
print(char,word)
