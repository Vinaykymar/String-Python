#Python Program to Count the Occurrences of
#Each Word in a Given String Sentence
words = raw_input("Enter a Statement:").split()
print(words)
count = 0
for word in words:
    print(word,"==>",words.count(word))
