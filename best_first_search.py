# CPSC 427 02
# Assignment #12: Best First Search with Alpha Beta Pruning
# Team Leader: Trevor Farthing (tfarthing)
# Developer 1: Dominic Soares
# Developer 2: Kevin Do
# To run: $ python3.6 best_first_search.py
import math

def main():
    graph = {'A' : ['P', 'B'],
             'B' : [5, 100],
             'C' : ['A', 'D', 'E'],
             'D' : ['R', 42],
             'E' : ['T', 'V'],
             'P' : [2, 3],
             'R' : [0],
             'T' : [2, 1],
             'V' : [9, 11]}

    #print best_first(graph,'C')
    print(alpha_beta('C', 3, (-1)*math.inf, math.inf, True, graph))
    
def best_first(graph, start):
    return 0

# Alpha-Beta pruning function
def alpha_beta(node, depth, alpha, beta, maxPlayer, graph):
    if depth == 0 or node.isdigit():
        return node
    if maxPlayer:
        v = math.inf*(-1)
        for child in graph[node]:
            v = max(v, alpha_beta(child, depth - 1, alpha, beta, False, graph))
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v
    else:
        v = math.inf
        for child in graph[node]:
            v = min(v, alpha_beta(child, depth - 1, alpha, beta, True, graph))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v
    
main()
