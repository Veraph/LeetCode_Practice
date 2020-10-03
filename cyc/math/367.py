# 367.py -- Valid Perfect Square

'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt
'''
def isPerfectSquare(num):
    for i in range(int(num ** 0.5 + 1)):
        if i * i == num:
            return True
    return False


# use math
    beg = 1
    while num > 0:
        num -= beg
        beg += 2
    return num == 0