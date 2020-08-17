# 345.py -- Reverse the vowels of a string

'''
Description:
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"
'''

def reverse_vowels(s):
    '''
    Vowels have both upper and lower cases.
    after the swap finished, i and j should also change
    j should equal to the length of string - 1
    '''
    if not s:
        return
    aux = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    len_str = len(s)
    i = 0
    j = len_str-1
    list_str = list(s)
    while i < j:
        if list_str[i] in aux and list_str[j] in aux:
            temp = list_str[i]
            list_str[i] = list_str[j]
            list_str[j] = temp
            i += 1
            j -= 1
        elif list_str[i] not in aux and list_str[j] not in aux:
            i += 1
            j -= 1
        elif list_str[i] not in aux:
            i += 1
        else:
            j -= 1
    return ''.join(list_str)