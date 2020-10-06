"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}  # empty dicitonary for verticies

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # if there is a v1 and v2
        if v1 in self.vertices and v2 in self.vertices:
            # connect them (add edge)
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make an empty queue
        q = Queue()

        # enque the starting vertex
        q.enqueue(starting_vertex)
        # variable for vertices already completed
        complete = set()

        # while the queus isn't empty
        while q.size() is not 0:
            # dequeue the first item
            currentVert = q.dequeue()
            # if not complete
            if currentVert not in complete:
                # print it
                print(currentVert)
                # add to complete
                complete.add(currentVert)
                # add neighbors of currentVert
                for nextVert in self.get_neighbors(currentVert):
                    if nextVert not in complete:
                        # add nextVert to queue
                        q.enqueue(nextVert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        '''
        - create an empty stack
        - create set to store visited nodes
        - push the starting vertex
        - while the stack size is not emty
            - pop the first item -> the current vertex
            - if it has not been visited
            - add it to visited
            - print the vertex
            - go thru all the neighbors of current vert
                - push next vertex to stack
        '''
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            currentV = s.pop()
            if currentV not in visited:
                visited.add(currentV)
                print(currentV)
                for neighborV in self.get_neighbors(currentV):
                    s.push(neighborV)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        My notes:
        - make a variable for an empty set
        - make visited = None initially
        -If visited is empty , make visited a set
        - if vert has not been visited
        - print and add it to visited
        - get all the neighbors of the vert
        - go thru all that vert's neighbors using this fn (neighbors, visited)

        """
        visited = None

        if visited == None:
            visited = set()
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            # get the neighbors
            neighborV = self.get_neighbors(starting_vertex)
            for neighbor in neighborV:
                self.dfs_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.

        My Notes:
        - make visited a set (keep track of all visited vertecies)
        - make path a list with the starting point inside
        - make a Queue
        - Add the path to the queue (enqueque)
        - while the queue size is not 0
            - dequeue the first (current) path in the path (first in first out)
            -current vertex is last in path
            -if at target, return to current path
        - if not visited, add to visited
        - get all the neighbors for current Vert
            - enqueue a new path for each neighbor to current path 
                -Note list + [item] returns a new list with the item added to the end without changing the original list (one line way)
                - using cloning way curretpath[:], append neighbor, enqueue clone
        """
        visited = set()
        path = [starting_vertex]
        q = Queue()
        q.enqueue(path)
        while q.size() > 0:
            currentPath = q.dequeue()
            currentV = currentPath[-1]
            if currentV == destination_vertex:
                return currentPath
            if currentV not in visited:
                visited.add(currentV)
            for nV in self.get_neighbors(currentV):
                # clone currentPath list using slice method
                clone = currentPath[:]
                clone.append(nV)
                q.enqueue(clone)
                # cloning using list + [item] method
            # q.enqueue(currentPath + [nV]) (indent one more)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        Notes: 
        -make a set for visited
        -make a path list with starting vertex inside
        -make a stack (last in first out)
        - push path into the stack
        - while the size of the stack is greater than 0 (empty)
            -current path is popped off of the stack
            - current vertex is the last in current path
            -if current vertex is the target
                -return the current path
            - if the vertex is not has not been visited
                - add it to visited 
            - go thru all neighbors for the current vertex
                - copy the current path and append the neighbor -- (so we won't change original path) -- and push it to the stack
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.

        Notes:
        - make visited = None initially
        - make path = None initially
        -If visited is empty , make visited a set
        - if vert has not been visited
            - add it to visited
        - if path is empty (None)
            - make path an empty list
        - make path = a clone of iteself with vertex appeneded and avoid issues
        - if vertex is target
            -return to the path
        - Go thru all the neighbors of the vert
            if target, append to path
                - return the path
            copy the path and append the neighbor
            then push it to the stack
        - return this function recursively(start, dest, path, visited)

        """
        pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
