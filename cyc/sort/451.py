# 451.py -- Sort Characters By Frequency
'''
Description:
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:
Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input:
"cccaaa"
Output:
"cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input:
"Aabb"
Output:
"bbAa"
Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''

def frequencySort(s):
    if not s:
        return ''
    '''
    method 1
    use dict to store the frequency and sort the dict.
    '''
    elets = list(s)
    elets.sort()
    freq = {}
    # input all values into the frequency dict
    for i in elets:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    # sort the dict and add items to the new list
    freq = {k:v for k, v in sorted(freq.items(), key=lambda x:x[1], reverse=True)}
    res = []
    for i, l in freq.items():
        res = res + [i] * l
    return ''.join(res)
    '''
    method 2
    use list and set
    '''
    s_set = set(s)
    res = []
    for i in s_set:
        res.append((i, s.count(i)))
    res.sort(key = lambda x:x[1], reverse=True)
    return ''.join(map(lambda x: x[0]*x[1], res))

    '''
    method 3
    use the built-in bucket sort function
    from collections import Counter
    '''
    return ''.join(key*freq for key,freq in Counter(s).most_common())

    

