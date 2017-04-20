# CPSC 427 02
# Assignment #12: Best First Search with Alpha Beta Pruning
# Team Leader: Trevor Farthing (tfarthing)
# Developer 1: Dominic Soares
# Developer 2: Kevin Do

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

    print best_first(graph,'A')

def best_first(graph, start):
    return 0
