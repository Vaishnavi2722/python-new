import re
str="""hello my number is 123456789
 and hello world my friend's number is 987654321 omh my god"""
reg='\d+'
match=re.findall(reg,str)
print(match)

reg2='\Ahello'
find2=re.findall(reg2,str)
print(find2)

str3="omgo, ort"
reg3='\b o'
find3=re.findall(reg3,str3)
print(find3)

