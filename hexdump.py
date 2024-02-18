#https://www.geeksforgeeks.org/command-line-arguments-in-python/
import sys

#https://stackoverflow.com/questions/1127905/how-can-i-format-an-integer-to-a-specific-length-in-javascript
def formatNumberLength(string, length):
    return "0" * (length - len(string)) + string

def formatASCIICode(asciiCode):
    if (asciiCode >= 17 and asciiCode <= 126):
        return chr(asciiCode)
    return "." 

#https://www.tutorialsteacher.com/python/python-read-write-file#:~:text=Writing%20to%20a%20Binary%20File,in%20binary%20format%20for%20writing.
#https://www.geeksforgeeks.org/reading-binary-files-in-python/
selectedFile = open(sys.argv[1], 'rb');

byteNumber = 0

readFile = selectedFile.read()

currentLineInText = ""
for currentByte in readFile:
    if byteNumber % 16 == 0:
        if byteNumber != 0:
            print(" |" + currentLineInText + "|");
            currentLineInText = ""

        print(formatNumberLength(f'{byteNumber:x}', len(f'{len(readFile)}')), end="  ")
    if byteNumber % 16 == 8:
        print (" ", end="")

    #https://stackoverflow.com/questions/16414559/how-to-use-hex-without-0x-in-python
    print(formatNumberLength(f'{currentByte:x}', 2), end=" ")
    byteNumber += 1
    
    #https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-find-ascii-value-character/#:~:text=chr%20()%20is%20a%20built,parameter%20is%20the%20ASCII%20code.
    currentLineInText += formatASCIICode(currentByte)

#print(byteNumber)
#print(currentLineInText, end="")
if byteNumber % 16 != 0:
    if byteNumber % 16 <= 7:
        print(" ", end="")
    print(("   " * (16 - byteNumber % 16)) + " |" + currentLineInText + "|");
