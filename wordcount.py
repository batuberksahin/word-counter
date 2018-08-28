import PyPDF2
import sys
import os.path

# Variables
maxKey = 0
orderedWords = {}
wordList = {}

# Open Pdf
def targetPdf(targetPdf):

    global pdfFile

    pdfFile = open(targetPdf, "rb")

# Counting Words
def countWord(targetWord = "null"):
    pdf = PyPDF2.PdfFileReader(pdfFile)

    # Split words from text
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        words = page.extractText().lower().split()
        for word in words:
            if word in wordList:
                wordList[word] += 1
            else:
                wordList[word] = 1

    # Order Dict
    for i in range(len(wordList)):
        global maxKey
        global maxWord
        maxKey = 0
        maxWord = ""

        for i in wordList:
            if maxKey == 0:
                maxKey = wordList[i]
                maxWord = i
            elif wordList[i] > maxKey:
                maxKey = wordList[i]
                maxWord = i

        orderedWords[maxWord] = maxKey
        wordList.pop(maxWord)

    # Print ranking
    for i in range(int(len(orderedWords) / 200)):
        print(str(i) + " : " + str(list(orderedWords.keys())[i]) + " (" + str(list(orderedWords.values())[i]) + " times)")

# Close pdf
def closePdf():
    pdfFile.close()

if __name__ == "__main__":
    # Command Line argument check
    if len(sys.argv) != 2:
        print("Usage: countword.py <pdf file>")
        sys.exit()

    if os.path.exists(sys.argv[1]):
        targetPdf(sys.argv[1])
        print("Words calculating..")
        countWord()
        closePdf()
    else:
        print(sys.argv[1] + " is doesnt exist!")
        sys.exit()