# 241.py -- Different Ways to Add Parentheses

'''
Description:
Given a string of numbers and operators, 
return all possible results from computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.

Example 1:
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''

def diffWaysToCompute(input):
    '''
    use the thinking of divide and conquer.
    divide the parent problem into sub problems and solve.
    DO NOT DIVE INTO TOO MUCH ABOUT THE DETAIL OF THE RECURSIVE,
    FOCUS ON THE THINKING.
    '''
    if input.isdigit():
        return [int(input)]
    res = []
    for i in range(len(input)):
        if input[i] in '-+*':
            res1 = diffWaysToCompute(input[:i])
            res2 = diffWaysToCompute(input[i+1:])
            for j in res1:
                for k in res2:
                    res.append(helper(j,k,input[i]))
    return res

def helper(m,n,op):
    if op == '-':
        return m-n
    elif op == '+':
        return m+n
    else:
        return m*n
diffWaysToCompute('2*3-4*5')