from functools import reduce 

def sortString (str):

              return reduce (lambda a, b : a + b, sorted (str))

str = input ("Enter a string that you want to arrange in alphabetical order:")

print (sortString (str))
