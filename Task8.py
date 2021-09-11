#Python Program to Take in Two Strings and Display the Larger
# String without Using Built-in Functions
s1 = raw_input("Enter String1:")
s2 = raw_input("Enter String2:")
count1 = 0
count2 = 0
for i in s1:
    count1 += 1
for j in s2:
    count2 += 1
if(count1<count2):
    print("Largest String is:",s2)
elif (count1==count2):
    print("both Strings are Equal:",s1)
else:
    print("Largest String is:",s1)

    
