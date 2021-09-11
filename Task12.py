s = raw_input("Enter a String:")#abc123
dcount = 0
lcount = 0
for ch in s:
    if ch.isdigit():
        dcount += 1
    elif(ch.isalpha()):
        lcount += 1
    else:
        pass
print("chr count is",dcount)    
