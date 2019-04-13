"""Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array 
if there are none. """


from collections import Counter

def anagrams(word, words):
    letters = Counter(word)
    result = [i for i in words if Counter(i) == letters]
    return result

# print(anagrams('abba',['aabb', 'abcd', 'bbaa', 'dada']))
