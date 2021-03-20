import re

Input = ''' 
•Put In your String here
'''
regexExpression = r'Put your regex here'

ro =re.compile(regexExpression)
fo =ro.findall(Input)

print(fo)