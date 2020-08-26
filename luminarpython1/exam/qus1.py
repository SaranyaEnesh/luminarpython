words="A,B,A,B,A,B,C,A,A,A"
dict={}
for word in words:
    if word not in words:
        dict[word]=1
    else:
        print("The most freequent character is",word)
        break
