import docx2txt
import collections

# uploading the CV and the Job Description

resume = docx2txt.process("DouglasLimaCV2021.docx").lower()
description = docx2txt.process("Senior Electrical Engineer - Grid Beyond.docx").lower()
uniqueWords = set()

# replacing characters non alphabetic per ' '

for eachChar in resume:
    if eachChar.isalpha() == False:
        resume = resume.replace(eachChar, ' ')

# picking the words from the document

for eachWord in resume.split(' '):
    if len(eachWord) > 2:
        if eachWord.isalpha():
            print(eachWord)
            uniqueWords.add(eachWord)

print(collections.Counter(sorted(uniqueWords)))