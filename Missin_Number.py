from itertools import accumulate 

def sortString (str):
    return tuple (accumulate (sorted (str)))[-1]

str = input ("Enter a string that you want to arrange alphabetically: ")

print (">>" + sortString (str))
