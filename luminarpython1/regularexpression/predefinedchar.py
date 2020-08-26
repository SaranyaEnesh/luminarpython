from re import *
#pattern="\s"#it will check for space
#pattern="\d"#it check digit[0-9]
#pattern="\D"#except digit[0-9]
#pattern="\w"#it will check all char and num,except spl char
pattern="\W"#it check spl char except char and num
matcher=finditer(pattern,"abc 7Zxy@4%")
for match in matcher:
    print(match.start())
    print(match.group())
