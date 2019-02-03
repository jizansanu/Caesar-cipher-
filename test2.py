word1 = input("Enter Your Word :")
s = int(input("Enter Shift Number :"))
j = 0
word2 = ""
for i in word1:
    n1 = ord(word1[j])
    n2 = n1 - s
    x=n2+26
    if (64 < n1 <91):
        if (64 < n2):
            word2 = word2 + chr(n2)
        else:
     	    word2 = word2 + chr(x)
        j=j+1
    elif (96 < n1 < 123):
        if (96 < n2):
            word2 = word2 + chr(n2)
        else:
            word2 = word2 + chr(x)
        j=j+1
print (word2)
