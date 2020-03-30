from edge import Edge


def costAcum(a, b):
    return a+b


def relAcum(a, b):
    return a * b


class MST:
    def __init__(self, cities, edges):
        self.cities = cities
        self.edges = edges

    def min_cost_tree(self):
        def selector(x): return x.c
        def accum(a, b): return a+b
        initial = 0
        return self.__kruskal(selector, accum, initial)

    def max_rel_tree(self):
        def selector(x): return -x.r
        def accum(a, b): return abs(a*b)
        initial = 1
        return self.__kruskal(selector, accum, initial)

    def __kruskal(self, selector, accum, initial):
        def recurse_fix(setPointers, u, v):
            fixKeys = []
            for key, value in setPointers.items():
                if value == setPointers[u]:
                    fixKeys.append(key)

            for key in fixKeys:
                setPointers[key] = setPointers[v]

        chosen_edges = []
        set_pointers = dict()
        total_weight = initial
        tree_size = len(self.cities) -1

        for vertex in self.cities:
            set_pointers[vertex] = vertex
            sorted_edges = sorted(self.edges, key=selector)

        for edge in sorted_edges:
            if(set_pointers[edge.u] != set_pointers[edge.v]):
                recurse_fix(set_pointers, edge.u, edge.v)

                total_weight = accum(selector(edge), total_weight)
                chosen_edges.append(edge)
                if len(chosen_edges) == tree_size:
                    return chosen_edges, abs(total_weight)

    
