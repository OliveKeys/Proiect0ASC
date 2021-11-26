import sys

def decrypt(password, inputFileName, outputFileName):
    inputFile = open(inputFileName, "rb")
    outputFile = open(outputFileName, "w")
    index = 0
    length = len(password)
    while True:
        letter = inputFile.read(1)
        if not letter:
            return
        letter = letter[0]
        letter = letter ^ ord(password[index])
        outputFile.write(chr(letter))
        index += 1
        if index == length:
            index = 0
    inputFile.close()
    outputFile.close()

inputFileName = sys.argv[1]
inputFileName += ".bin"
password = sys.argv[2]
outputFileName = sys.argv[3]
decrypt(password, inputFileName, outputFileName)

