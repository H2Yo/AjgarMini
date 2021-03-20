#!python3
#regexProj2_StronPasswordDetection.py - This Program makes sure the password
# string it is passed is strong. A strong password is defined as one that starts with a letter, is at
# least eight characters long, contains both uppercase and lowercase characters,
# and has at least one digit

import re

while True:
    inputString = input('Enter Password :\n')

    #RegexMatches
    ro1 = re.compile(r'^\S{8,}$')
    ro2 = re.compile(r'[A-Z]+')
    ro3 = re.compile(r'[a-z]')
    ro4 = re.compile(r'\d+')
    ro5 = re.compile(r'^[A-Za-z]')

    mo1 = ro1.search(inputString)
    mo2 = ro2.search(inputString)
    mo3 = ro3.search(inputString)
    mo4 = ro4.search(inputString)
    mo5 = ro5.search(inputString)

    print('\nRESULT\n'+'-'*100 )
    if mo1 and mo2 and mo3 and mo4 and mo5:
        print('Valid Password\n')
    else:
        print('''Wrong PassWord Entered . 
A strong password is defined as one that is atleast eight characters long, contains both uppercase and lowercase characters,and has at least one digit)\n''')
    print('-'*100)
    looper = input('Press E to exit. Anything else to try another password \n')
    if looper.lower() == 'e':
        break
