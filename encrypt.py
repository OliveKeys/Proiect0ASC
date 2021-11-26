import sys

def encrypt(password, inputFileName, outputFileName):
    inputFile = open(inputFileName, "r")
    outputFile = open(outputFileName, "wb")
    index = 0
    length = len(password)
    while True:
        letter = inputFile.read(1)
        if not letter:
            return
        letter = ord(letter) ^ ord(password[index])
        outputFile.write(letter.to_bytes(1, 'big'))
        index += 1
        if index == length:
            index = 0
    inputFile.close()
    outputFile.close()

password = sys.argv[1]
inputFileName = sys.argv[2]
outputFileName = sys.argv[3]
outputFileName += ".bin"
encrypt(password, inputFileName, outputFileName)
	
