# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError
from Queue import PriorityQueue
from Queue import *
from graph_adjacency_list import Graph

def shortest_path(graph, source, target):
    # `graph` is an object that provides a get_neighbors(node) method that returns
    # a list of (node, weight) edges. both of your graph implementations should be
    # valid inputs. you may assume that the input graph is connected, and that all
    # edges in the graph have positive edge weights.
    # 
    # `source` and `target` are both nodes in the input graph. you may assume that
    # at least one path exists from the source node to the target node.
    #
    # this method should return a tuple that looks like
    # ([`source`, ..., `target`], `length`), where the first element is a list of
    # nodes representing the shortest path from the source to the target (in
    # order) and the second element is the length of that path
    #
    # NOTE: Please see instructions.txt for additional information about the
    # return value of this method.

    # traverse graph with bfs, set shortest_distance for each node to inf
    visited = []  # track visited nodes
    shortest_distance = {} 
    q = Queue()
    all_nodes = set()
    
    q.put(source)
    # all_nodes.add(source)

    # set all nodes shortest distance to inf
    while not q.empty():
        curr_node = q.get()
        
        if curr_node not in visited:
            visited.append(curr_node)
            neighbors = graph.get_neighbors(curr_node)
            if neighbors:
                for neighbor_node, weight in neighbors:
                    q.put(neighbor_node)
                    # all_nodes.add(neighbor_node)
                    shortest_distance[neighbor_node] = float('inf')

    # implement Djijkstra's algo
    short_path = []
    pq = PriorityQueue()  # track which node to visit next
    previous_node = {}
    visited = []  # reset visited nodes list
    
    shortest_distance[source] = 0

    pq.put((shortest_distance[source], source))

    while not pq.empty():
        frontier_edge = pq.get()  
        curr_node = frontier_edge[1]
        
        if curr_node not in visited:
            visited.append(curr_node)
        
            # add all its neighbors to the pq
            neighbors = graph.get_neighbors(curr_node)
            
            if neighbors:
                for neighbor_node, neighbor_dist in neighbors:
                    
                    proposed_dist = shortest_distance[curr_node] + neighbor_dist
                    # add the frontier_edge
                    # which will prioritize on proposed edge distance, not just the edge weight
                    pq.put((proposed_dist, neighbor_node))  

                    if proposed_dist < shortest_distance[neighbor_node]:
                        shortest_distance[neighbor_node] = proposed_dist
                        previous_node[neighbor_node] = curr_node
                
    # work backgrounds through the previous node dict and save path    
    curr = target
    while curr != source:
        short_path.insert(0, curr)  # insert at beginning of list
        curr = previous_node[curr]  # get previous node
    short_path.insert(0, curr)  # insert the last, source node
    
    return (short_path, shortest_distance[target])

adjacency_graph = Graph()



##
# adjacency_graph.add_edge('a', 'c', 15)
# adjacency_graph.add_edge('b', 't', 1)
# adjacency_graph.add_edge('d', 't', 1)
# adjacency_graph.add_edge('a', 't', 21)
# adjacency_graph.add_edge('b', 'u', 1)
# adjacency_graph.add_edge('b', 't', 6)
# adjacency_graph.add_edge('u', 't', 2)
# adjacency_graph.add_edge('c', 't', 20)

# print shortest_path(adjacency_graph, 'a', 't')


graph1 = Graph()
graph1.add_edge('t', 'a', 5)
graph1.add_edge('a', 'c', 10)
graph1.add_edge('c', 'd', 6)
graph1.add_edge('d', 'e', 12)
graph1.add_edge('t', 'd', 2)

path = shortest_path(graph1, 't', 'e')
print path        
                
                
             
