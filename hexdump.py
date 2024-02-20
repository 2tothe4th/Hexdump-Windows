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
selectedFile = "";

flags = []

#https://www.w3schools.com/python/ref_func_range.asp
for i in range(1, len(sys.argv)):
    currentWord = sys.argv[i]
    if currentWord[0] == "-":
        #https://www.w3schools.com/python/python_lists_add.asp       
        flags.append(currentWord[slice(1, len(currentWord))].lower())        
    else:
        selectedFile = open(currentWord, 'rb')
#print(flags)

byteNumber = 0

readFile = selectedFile.read()

currentLineInText = ""
currentLineInConsole = ""
last16Bytes = []

lastTwoLinesAreRepeated = False

settings = ["noascii" in flags]

for currentByte in readFile:
    if byteNumber % 16 == 0:
        currentLineInConsole += formatNumberLength(f'{byteNumber:x}', len(f'{len(readFile):x}')) + "  " 
    if byteNumber % 16 == 8:
        currentLineInConsole += " "

    #https://stackoverflow.com/questions/16414559/how-to-use-hex-without-0x-in-python
    currentLineInConsole += formatNumberLength(f'{currentByte:x}', 2) + " "
    byteNumber += 1

    #https://www.toppr.com/guides/python-guide/examples/python-examples/python-program-find-ascii-value-character/#:~:text=chr%20()%20is%20a%20built,parameter%20is%20the%20ASCII%20code.
    currentLineInText += formatASCIICode(currentByte)
    
    current16Bytes = readFile[slice(byteNumber - 16, byteNumber)]
    if byteNumber % 16 == 0 and byteNumber != 0:
        if not settings[0]:
            currentLineInConsole += " |" + currentLineInText + "|";
            currentLineInText = ""
    
        #https://www.w3schools.com/python/ref_func_slice.asp
        if current16Bytes == last16Bytes and not lastTwoLinesAreRepeated:
            print("*")
            lastTwoLinesAreRepeated = True
        elif current16Bytes != last16Bytes:
            print(currentLineInConsole)                    
            lastTwoLinesAreRepeated = False

        currentLineInConsole = ""
        last16Bytes = current16Bytes

print(currentLineInConsole, end="")
if byteNumber % 16 != 0 and not settings[0]:
    if byteNumber % 16 <= 7:
        print(" ", end="")
    print(("   " * (16 - byteNumber % 16)) + " |" + currentLineInText + "|")

print(f'{byteNumber:x}')
