# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 13:53:48 2014

@author: lseshan
"""
GRAPH3 = {0: set([]),
          1: set([2]),
          2: set([1]),
          3: set([4]),
          4: set([3])}
GRAPH2 = {1: set([2, 4, 6, 8]),
          2: set([1, 3, 5, 7]),
          3: set([2, 4, 6, 8]),
          4: set([1, 3, 5, 7]),
          5: set([2, 4, 6, 8]),
          6: set([1, 3, 5, 7]),
          7: set([2, 4, 6, 8]),
          8: set([1, 3, 5, 7])}
          
GRAPH0 = {0: set([1]),
          1: set([0, 2]),
          2: set([1, 3]),
          3: set([2])}          

             
from collections import deque
def bfs_visited(ugraph, start_node):
    """
        bfs_visited: returns bfs traversed neighbours
    """
    visited_set = set([start_node])
    visited_list = [start_node]
    not_visited_q = deque()
    not_visited_q.append(start_node)
    print "not_visited",not_visited_q
    while not_visited_q:
        node_to_visit = not_visited_q.popleft()
        neigh_set   = ugraph[node_to_visit]
        for neighbour in neigh_set:
            if neighbour not in visited_set:
                print neighbour
                visited_set.add(neighbour)
                visited_list.append(neighbour)
                not_visited_q.append(neighbour)
    print visited_list
    return visited_set
    
def cc_visited(ugraph):
    """
        cc_visited: returns cc of a given graph
    """
    print ugraph.keys()
    remaining_nodes  = (ugraph.keys())
    print "remain",remaining_nodes
    conn_comp=[]
    while remaining_nodes:
        remaining_nodes_before = remaining_nodes
        random_node = remaining_nodes.pop()
        print "remain_nodes:loop",remaining_nodes
        #random_node = remaining_nodes[1:]
        print "random",random_node
        visited_set = bfs_visited(ugraph, random_node) 
        conn_comp.append(visited_set)
        remaining_nodes = set(remaining_nodes_before)-visited_set
        #remaining_nodes = list.append(remaining_nodes)
    return conn_comp

def largest_cc_size(ugraph):
    """
        largest_cc_size: compute cc_size
    """
    conn_comp = cc_visited(ugraph)
    max_cc = 0
    for each_set in conn_comp:
        print each_set,len(each_set)
        if (max_cc< len(each_set)):
            max_cc = len(each_set)
    return max_cc
    
def compute_resilience(ugraph, attack_order):
    """
        compute_resilience: computes the resilience of the graph
    """
    print attack_order
    dummy_k = 0
    res_graph=[]
    res_graph.append(largest_cc_size(ugraph))
    for node in attack_order:
        dummy_k = dummy_k+1
        ugraph.pop(node)
        for each_node in ugraph:
            edge_set = ugraph[each_node]
            if node in edge_set:
                edge_set.remove(node)
        print largest_cc_size(ugraph)
        res_graph.append(largest_cc_size(ugraph))
    return res_graph
                    
        
    
print bfs_visited(GRAPH2, 1)

print "Conn Comp:"
print cc_visited(GRAPH2)
#print largest_cc_size(GRAPH2)
#print compute_resilience(GRAPH0, [1, 2])

            