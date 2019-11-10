########################################################
# This is a basic lexicon based sentiment analysis. Using lexicon created by
# github user mkulakowski2 (https://gist.github.com/mkulakowski2/4289441)
# this code gives a sentence an overall "sentiment" score (positive words + negative words).
#
#
#
########################################################

#definition of variables and lists
positiveWords = []
negativeWords= []
#counter of positive and negative words
cntPos = 0
cntNeg = 0
#overall score(postive words + negative words)
overallScore = 0

# Reads text file
with open('pos.txt', 'r') as positiveFile:
    #iterate through the positive words
    for line in positiveFile:
        #removes linebreaks
        currentPlace = line[:-1]
        #appends all positive words into positive list
        positive.append(currentPlace)

with open('neg.txt', 'r') as negativeFile:
    for line in negativeFile:
        currentPlace = line[:-1]
        negative.append(currentPlace)


getSentence = raw_input("Give me sentence  ")
#adds all of the words in the user's sentence into a list
sentenceList = getSentence.split()

#iterates through the words in the sentence, and checks if they are either positive or negative
for i in sentenceList:
    if i in positive:
        cntPos+=1
        print (i)
    if i in negative:
        cntNeg -= 1
        print (i)

#the higher the overall score, the more positive a sentence is and vice versa
overallScore = cntPos + cntNeg
if (overallScore < 0):
    print("Neg ", str(overallScore))
else:
    print("Pos " + str(overallScore))
