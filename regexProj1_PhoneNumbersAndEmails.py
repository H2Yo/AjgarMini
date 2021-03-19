#!python3
#regexProj1_PhoneNumbersAndEmails - Reads the cipboard for text with phones and Emails and extracts those out from the text for you!!

import re,pyperclip

#Pull Text from clipboard
inputString = pyperclip.paste()

#Regex for Phones ()
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

#Regex for Emails
eMailRegex = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.\w{2,4}')

#Get matches
phones = re.findall(phoneRegex, inputString)
mails = re.findall(eMailRegex , inputString)

phoneStr = 'The phone numbers found are :\n{}'.format(','.join([x[0] for x in phones])) if phones else 'No Phones found'
mailStr = '\nThe emails found are : \n{}'.format(','.join(mails)) if mails else '\nNo Mails Found'

#Paste to Clipboard
# pyperclip.copy(phoneStr+mailStr)
print(phoneStr+mailStr)