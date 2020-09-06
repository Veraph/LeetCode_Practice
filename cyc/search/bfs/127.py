# 127.py -- Ward Ladder

'''
Description:
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
import collections, string
def ladderLength(beginWord, endWord, wordList):
    '''
    time out.
    reason is if the length of th wordlist is very big!
    different from pure list and set(),
    we try to use deque() now.
    '''
    wordList = set(wordList)
    q = collections.deque([(beginWord,1)])
    alpha = string.ascii_lowercase # 'abc...z'
    used = set()
    while q:
        word, cnt = q.popleft()
        if word == endWord:
            return cnt
        
        for i in range(len(word)):
            for ch in alpha:
                chc_word = word[:i] + ch + word[i+1:]
                if chc_word in wordList and chc_word not in used:
                    q.append((chc_word, cnt+1))
                    used.add(chc_word)
    return 0


        
