# 93.py -- Restore IP Addresses

'''
Desciption:
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. 
You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, 
separated by single dots and cannot have leading zeros. 
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and 
"0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "1111"
Output: ["1.1.1.1"]

Example 4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]

Example 5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 
Constraints:
0 <= s.length <= 3000
s consists of digits only.
'''

def restoreIpAddresses(s):
    '''
    mind the position of return
    when return, the current recursion terminated.
    if you want to call recursion, just call the function.
    '''
    res = []

    def dfs(s,index,comb,res):
        if index == 4:
            if not s:
                res.append(comb[:-1])
            return 
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    dfs(s[i:], index+1, comb+s[:i]+'.', res)
                elif i == 2 and s[0] != '0':
                    dfs(s[i:], index+1, comb+s[:i]+'.', res)
                elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                    dfs(s[i:], index+1, comb+s[:i]+'.', res)
    
    dfs(s, 0, '', res)
    return res
