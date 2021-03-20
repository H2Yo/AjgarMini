#!python3
#regexProj2_URLExtract.py - Used to extract URLs from a text in clipboard

import re,pyperclip

#Take input from clipboard
inputString = pyperclip.paste()

#Write Regex for URLs and Search

ro = re.compile(r'(http(s)?://(\S)+)')
result = ro.findall(inputString)

#Print out (or paste to clipboard) all URLs line by line
if result:
    print('The Extracted URLs are : \n')
    print(*(x[0] for x in result),sep= '\n')
else:
    print('No Matches Found')
