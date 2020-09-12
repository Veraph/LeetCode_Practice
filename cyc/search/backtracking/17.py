# 17.py -- Letter Combinations of a Phone Number

'''
Description:
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

def letterCombinations(digits):
    '''
    simple iteration
    '''
    
    if not digits:
        return []
    # create a phone dict
    dict_phone = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    l = len(digits)
    res = []
    
    def dfs(index,comb,res):
        if len(comb) == l:
            res.append(comb)
            return
        for i in dict_phone[digits[index]]:
            dfs(index+1, comb+i, res)
    
    dfs(0,'',res)
    return res
        
