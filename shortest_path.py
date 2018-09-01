# Please see instructions.txt for the description of this problem.
from exceptions import NotImplementedError
from Queue import PriorityQueue, Queue

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

  # YOUR CODE HERE
  
  
  # First run BFS to obtain the vertex set V
  V = set()
  q = Queue()
  q.put(source)
  V.add(source)
  while not q.empty():
    v = q.get()
    neighbors = graph.get_neighbors(v)
    if neighbors:
      for neighbor in neighbors:
        if neighbor[0] not in V:
          q.put(neighbor[0])
          V.add(neighbor[0])

  # Time to run Dijkstra's
  dist = {v : float('inf') for v in V}
  dist[source] = 0.0

  prev = {v : -1 for v in V} # -1 is just a dummy value

  # We'll use a Priority Queue. Assign priority using distance from source
  pq = PriorityQueue()
  pq.put((dist[source],source))
  visited = set()

  # Now we get to the loop.
  while not pq.empty():
    u = pq.get()
    if u[1] not in visited: # If we haven't considered u's neighbors already
      visited.add(u[1])
      neighbors = graph.get_neighbors(u[1])
      if neighbors:
        for v in neighbors:
          alt = dist[u[1]] + v[1]
          if alt < dist[v[0]]:
            dist[v[0]] = alt
            prev[v[0]] = u[1]
            pq.put((dist[v[0]],v[0]))

  # Backtrack through prev to obtain the path
  path = [target]
  curr = target
  while curr != source:
    curr = prev[curr]
    path.append(curr)

  path = path[::-1] # Path is backwards, so reverse it!

  return path, dist[target]








