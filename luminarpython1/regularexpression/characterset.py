from re import *
pattern='[abc]'#itwill check either a,b,or c
#pattern='[a-z]'#lower case letters
#pattern='[A-Z]'#upper case letters
#pattern='[a-zA-Z]'#it will check all alphabets
#pattern='[0-9]'#print digit
#pattern='[^0-9]'#except digit
#pattern='[^a-zA-Z0-9]'#except numbers and letters/print special char
matcher=finditer(pattern,"abx 7Zx$y@#")
for match in matcher:
    print(match.start())
    print(match.group())
