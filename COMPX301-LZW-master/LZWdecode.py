# COMPX301-20A Lee So 1364878

import fileinput

codes = []
outData = ""
prevString = ""
dicSize = 256  # this stands for dictionary size haha yes
nextCode = dicSize

# initialize the dictionary
dictionary = dict([(x, chr(x)) for x in range(dicSize)])

# read through the encoder's output
try:
    for line in fileinput.input():
        code = int(str.rstrip(line))  # strip newlines etc. and convert to int
        codes.append(code)

except Exception as e:
    print(e)
    exit

# for each code we now have...
try:
    for code in codes:
        if not (code in dictionary):
            dictionary[code] = prevString + (prevString[0])
        outData += dictionary[code]
        if not (len(prevString) == 0):
            dictionary[nextCode] = prevString + (dictionary[code][0])
            nextCode += 1
        prevString = dictionary[code]

    print(outData, end='')

except Exception as e:
    print(e)
