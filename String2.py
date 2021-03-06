#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
import re

def verbing(s):
    if len(s)>=3:
        result=re.search('ing',s)
        try:
            a=result.group()
            flag=1
        except:
            flag=0
            pass
        if flag==1:
            s=s+'ly'
        else:
             s=s+'ing'
        return(s)
    else:
        return(s)


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    rep=re.sub(r'(.*)(not)(.*)(bad)',r'\1good',s)
    return(rep)


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(s, c):       
    slen=len(s)
    clen=len(c)
    if len(s)%2==0:
        firsthalf=s[0:int(slen/2)]
        secondhalf=s[int(slen/2):]
        #print(firsthalf,secondhalf)
    else:
        #print(int(slen/2))
        firsthalf=s[0:int(slen/2)+1]
        secondhalf=s[int(slen/2)+1:]
        #print(firsthalf,secondhalf)
    
    if len(c)%2==0:
        firsthalfc=c[0:int(clen/2)]
        secondhalfc=c[int(clen/2):]
        #print(firsthalfc,secondhalfc)
    else:
        firsthalfc=c[0:int(clen/2)+1]
        secondhalfc=c[int(clen/2)+1:]
        #print(firsthalfc,secondhalfc)
        
    return(firsthalf+firsthalfc+secondhalf+secondhalfc)


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
      prefix = ' OK '
    else:
      prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print ('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    
    print ('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")
    
    
    print ('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
