# 785.py -- Is Graph Bipartite

'''
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.
'''

def isBipartite(graph):
    '''
    The idea behind this one is to color the nodes with two different colors.
    The process is:
    when we find a node with val 0(which means it is not colored),
    we can color it to 1(black), then all node adjancent to it will be colored as -1(white),
    after the process, we will try to find out whether there are adjancent nodes with the same color.
    '''

    ## dfs method
    n = len(graph)
    color = [0] * n

    def dfs(node, clr):
        # if it is colored, compare the colored with the color should be
        # this check should be in a new dfs
        if color[node]:
            return color[node] == clr

        # color the node, and iterate the node's adjancent nodes
        color[node] = clr
        for i in graph[node]:
            if not dfs(i, -clr):
                return False
        return True
    
    # iterate every node
    for i in range(n):
        if not color[i] and not dfs(i, 1):
            return False   
    return True

    ## bfs method
    n = len(graph)
    color = [0] * n
    
    # iterate through the nodes
    for i in range(n):
        if color[i]: continue
        queue, color[i] = [i], 1
        while queue:
            node = queue.pop()
            # iterate through the adjancent nodes
            for i in graph[node]:
                if not color[i]:
                    color[i] = -color[node]
                    queue.append(i)
                elif color[i] != -color[node]:
                    return False
    return True

        
    