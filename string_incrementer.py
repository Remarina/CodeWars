"""
Your job is to write a function which increments a string, to create a new string. 
If the string already ends with a number, the number should be incremented by 1. 
If the string does not end with a number the number 1 should be appended to the new string.

"""
import re

def increment_string(string):
    digits = ''.join(re.findall('\d*$', string))
    if digits == '':
        return string + '1'
    else:
        new_digits = str(int(digits) + 1).zfill(len(digits))
        return string[:-len(digits)] + new_digits


print(increment_string('foo4bar0099'))
print(increment_string('1fo7o84bar99'))
