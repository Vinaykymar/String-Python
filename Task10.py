#Python Program to Check if a String is a Palindrome or Not
s = raw_input("Enter string:")
if(s == s[::-1]):
   print("Given string is a palindrome")
else:
      print("Given string isn't a palindrome")
