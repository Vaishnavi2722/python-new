import re
str="hello world, i am here"
match=re.search('hello',str)
print(match)
#print('start index:',match.start())
#print('end index:',match.end())