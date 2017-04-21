# CPSC 427 02
# Assignment #12: Best First Search with Alpha Beta Pruning
# Team Leader: Trevor Farthing (tfarthing)
# Developer 1: Dominic Soares
# Developer 2: Kevin Do
# To run:  Enter in the goal state in the best_first function call (last line of main)
#          Then run $ python3.6 best_first_search.py
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

    # Will be AB-pruned graph with values(alpha/beta) added at each node
    new_g = {}
    print(alpha_beta('C', 3, (-1)*math.inf, math.inf, True, graph, new_g))
    print(new_g)
    # ENTER IN GOAL NODE AS 4TH PARAMETER
    print(best_first(graph, new_g, 'C', 3))
          
def best_first(graph, new_graph, start, goal):
    closed = []
    opn = [start]
    scores = {} 
    while opn:
        # Choose to explore node with shortest path
        curr = min(opn, key=lambda x:new_graph[x])
        if curr == goal:
            return closed
        closed.append(curr)
        opn.remove(curr)

        if curr in graph:
            for child in graph[curr]:
                if not child in closed and child in new_graph:
                    opn.append(child)
    return closed
            

# Alpha-Beta pruning function
def alpha_beta(node, depth, alpha, beta, maxPlayer, graph, new_graph):
    if depth == 0 or node.isdigit():
        new_graph[node] = node
        return node
    if maxPlayer:
        v = math.inf*(-1)
        for child in graph[node]:
            v = max(v, alpha_beta(child, depth - 1, alpha, beta, False, graph, new_graph))
            alpha = max(alpha, v)
            # set value for node in pruned graph
            new_graph[node] = v
            if beta <= alpha:
                break
        return v
    else:
        v = math.inf
        for child in graph[node]:
            v = min(v, alpha_beta(child, depth - 1, alpha, beta, True, graph, new_graph))
            beta = min(beta, v)
            # set value for node in pruned graph
            new_graph[node] = v
            if beta <= alpha:
                break
        return v
    
main()
