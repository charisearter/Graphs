'''
1. Make Graph class

Find earliest ancestor psudocode
Hints: keep track of longest list, last number in longest list is earliest ancestor
Hint2: do depth first and keep track of depth, highest depth would be earliest ancestor(s)

'''


class Graph:
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, vertex):
        self.verticies[vertex] = []

    def add_edge(self, v1, v2, connection):  # store child/parent connect with ID
        # store v2 & connection as set... key is connection string
        self.verticies[v1].append((v2, connection))

    def get_neighbors(self, vertex):  # give me the vertex's neighbors
        return self.verticies[vertex]

    def the_parent(self, edge):  # are they they parent or not
        if edge[1] == 'parent':
            return True
        else:
            return False

    # depth first search traversal for ancestors
    def dft_ancestors(self, v, paths, longest, path=None):
        if path is None:  # make a list if no path
            path = []

        # make new path for current vertex(v) and append to path
        path = path + [v]

        n = self.get_neighbors(v)  # give me all the vertex neighbors

        # filter the ones with parents because I only want ancestors
        # list because I want to check length of list
        parents = list(filter(self.the_parent, n))

        if len(parents) == 0:  # no parents / if earliest ancestor
            if len(paths) > longest:  # if paths is larger than longest
                longest = len(paths)  # the paths is the new value of longest
                paths = [path]  # longest path replaces whatever was in paths
            else:  # otherwise
                paths.append(path)  # add path to the end of paths
            return  # no parents left to look thru
        for p in parents:  # go thru parents to find earliest ancestor recursively
            self.dft_ancestors(p[0], paths, longest, path)


def earliest_ancestor(ancestors, starting_node):
    g = Graph()  # make a graph

    for a in ancestors:  # look thru ancestors
        p, c = a  # parent (p), child (c) = ancestor (a)

        if p not in g.verticies:  # if parent is not in the graph
            g.add_vertex(p)  # add the parent to the graph

        # add connection from parent to child, label child (connection)
        g.add_edge(p, c, 'child')

        if c not in g.verticies:  # if child is not in graph
            g.add_vertex(c)  # add to child to graph

        # add connection from child to parent, label parent as parent (connection)
        g.add_edge(c, p, 'parent')

    paths = []  # store all paths here

    longest = 0  # store length of longest path here, initially starts as 0

    # dft ancestors of start node
    g.dft_ancestors(starting_node, paths, longest)

    if len(paths) > 1:  # more than 1 longest path
        ancestors = []  # store the oldest ancestors in the list

        for path in paths:  # look thru paths
            # add the ancestor to the very end of list
            ancestors.append(path[-1])
        # return the smallest ancestor (smallest argument)
        return min(ancestors)

    if len(paths[0]) == 1:  # if there is only one path and no ancestors
        return -1  # return -1
    else:  # otherwise
        return paths[0][-1]  # return last ancestor in the path
    # path[0] --> index 0 of paths 
    # path[-1] --> very last index in array
