import pylab

# You may have to change this path
WORDLIST_FILENAME = "/home/csd/6002x/L4P5/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vals = []
    for word in wordList:
        temp = 0.0
        for letter in word:
            if letter in ['a', 'e', 'i', 'u', 'o']:
                temp += 1
        vals.append(temp/len(word))
    temp = 0.0
    for prop in vals:
        if prop < 0.5:
            temp += 1 
    less_prop = temp / len(vals)   
    pylab.figure()
    pylab.hist(vals, bins = 10)
    pylab.xlabel('the proportion of vowels in each word')
    pylab.ylabel('Number of words')
    xmin, xmax = pylab.xlim()
    ymin, ymax = pylab.ylim()
    pylab.text(xmin + (xmax-xmin)*0.63, (ymax-ymin)/2,
               'Vovel proportion less than 0.5\ntotally is '+
               str(less_prop))
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
