#!python3
#workingWithFilesProj1_RandomQuizFiles - this file generates 35 different quiz files each having 50 questions 
# each asking the capital of a US state. Questions are shuffled so students can't cheat. 
# It gives answer keys for each quizfile as well


import random
from pathlib import Path
import os.path as osp
import os

quizfilePath = Path('../WorkingWithFiles/Quiz_Files/')
answerKeyFilePath = Path('../WorkingWithFiles/Answer_Files/')
if not quizfilePath.exists():
    os.makedirs(str(quizfilePath))
if not answerKeyFilePath.exists():
    os.makedirs(str(answerKeyFilePath))

statesAndCaps = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

statesList = list(statesAndCaps.keys())
capitalsList = list(statesAndCaps.values())
# print(statesList)
for quizNum in range(35):
    print('Working on file number - {}'.format(quizNum+1))
    #shuffle states
    random.shuffle(statesList)
    # print(statesShuffled)
    #Create Quiz File and write Header
    
    thisFile = open((quizfilePath/'Quiz_{}.txt'.format(quizNum+1)),'w')
    thisFile.write('\t'*7 + 'Quiz Number - {}\n'.format(quizNum+1) + '-'*120 +'\n\nTime : 30 mins\n\n' + 'Choose the correct Capital of the US states!!Enjoy!!\n\n')
    
    thisAnsFile = open(answerKeyFilePath/'Quiz_{}_Answer_Key.txt'.format(quizNum+1),'w')
    thisAnsFile.write('\t'*7 + 'Answers to Quiz Number - {}\n'.format(quizNum+1) + '-'*120 +'\n\n')
    #for each state, get one correct and 3 incorrect answers and write the question and options in the quiz file
    for quesNum,thisState in enumerate(statesList):     
        # print(thisState)
        thisFile.write('\n Ques.{} - What is the Capital of {} ? :\n'.format(quesNum+1,thisState))
        thisCorrectAnswer = statesAndCaps[thisState]
        optionsDict = {0:'A',1:'B',2:'C',3:'D'}
        otherOptions = random.sample([x for x in capitalsList if x != thisCorrectAnswer],3)
        optionSet = [thisCorrectAnswer] + otherOptions
        # print(optionSet,otherOptions)
        random.shuffle(optionSet)
        optionString = ''
        for i in range(4):
            optionString = optionString + '('+ optionsDict[i] + ')' + optionSet[i] + '\t'            
        thisFile.write(optionString + '\n')
        thisAnsFile.write('{}.{}\n'.format(quesNum+1,optionsDict[optionSet.index(thisCorrectAnswer)]))
    thisFile.write('\n\n' + '\t'*5 + '--END--')
    thisFile.close()
    thisAnsFile.write('\n\n' + '\t'*5 + '--END--')
    thisAnsFile.close()
print('DONE')