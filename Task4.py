string=raw_input("Enter string:")
ovelstr = "aeiouAEIOU"
count = 0
for ch in string:
    if ch in ovelstr:
       count += 1
print(count)
 
