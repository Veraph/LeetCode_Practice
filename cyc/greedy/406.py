# 406.py -- Queue Reconstruction by Height

'''
Description:
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), 
where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

def reconstructQueue(people):
    '''
    sort people with decreasing height first,
    if have same height, sort with increasing index instead.
    then insert each elements with their index one by one,
    later elements insertion wont influence the previous elements beacause bigger one inserted already.
    '''
    people.sort(key=lambda x: (-x[0], x[1]))
    res = []
    for p in people:
        res.insert(p[1], p)
    return res