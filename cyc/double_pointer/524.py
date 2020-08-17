# 524.py -- Longest word in dictionary through deleting

'''
Description:
Given a string and a string dictionary, 
find the longest string in the dictionary 
that can be formed by deleting some characters of the given string. 
If there are more than one possible results, 
return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output: 
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]
Output: 
"a"

Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
'''

def findLongestWord(s,d):
    '''
    be familiar about how the lambda works.
    take care of the change of index.
    '''
    d.sort(key=lambda x: (-len(x),x)) # sort with the length first and then with the alphabatic order
    for i in d:
        len_s = len(s)-1
        len_i = len(i)-1
        while len_s >= len_i:
            if len_i < 0:
                return i
            if s[len_s] == i[len_i]:
                len_i -= 1
                len_s -= 1
            else:
                len_s -= 1
    return ''



    
