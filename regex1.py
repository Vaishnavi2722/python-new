import re
str="""hello my number is 123456789
 and my friend's number is 987654321"""
reg='\d+'
match=re.findall(reg,str)
print(match)