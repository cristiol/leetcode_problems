"""
Given an input string, write a function that returns the Run Length Encoded string for the input string.
For example, if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6”

Follow the steps below to solve this problem:

Pick the first character from the source string.
Append the picked character to the destination string.
Count the number of subsequent occurrences of the picked character and append the count to the destination string.
Pick the next character and repeat steps 2, 3 and 4 if the end of the string is NOT reached.
"""


def encodeString(stringVal):
    # Your code goes here.
    i = 0
    count = 0
    res = []

    while i < len(stringVal) - 1:
        if stringVal[i] == stringVal[i+1]:
            count += 1
        else:
            res.append((stringVal[i], count))
            count = 1
        i += 1
    res.append((stringVal[i], count))

    return res


def decodeString(encodedList):
    # Your code goes here.
    return ''.join([k*v for k, v in encodedList])


encodeString = encodeString('AAAAAABBBAAA')
print(decodeString(encodeString))