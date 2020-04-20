
class RelCalculator:
    def __init__(self, cities):
        self.cities = cities
        self.treeSize = len(cities) - 1

    def recursive_rel(self, edges, factored_edges):
        # when the graph is a tree
        def simple_rel(edges):
            accum = 1

            for edge in edges:
                accum *= edge.r

            return accum

        # check if the graph is connected
        def is_connected(edges):
            def dfs(source, edges, visited):
                visited[source] = True

                for edge in filter(lambda x:  x.u == source, edges):
                    if not visited[edge.v]:
                        dfs(edge.v, edges, visited)

                for edge in filter(lambda x:  x.v == source, edges):
                    if not visited[edge.u]:
                        dfs(edge.u, edges, visited)

            visited = dict()

            for city in self.cities:
                visited[city] = False

            dfs(self.cities[0], edges, visited)

            return all(visited.values())


        if(len(edges) + len(factored_edges) == self.treeSize) and is_connected(edges + factored_edges):
            return simple_rel(edges)
        else:
            if(len(edges) > 0):
                first = edges[0]
                tail = edges[1:]

                # edge decomposition
                # first step remove the edge and see the cost and then return the edge as a factored_edge
                total = 0
                total += (1 - first.r) * self.recursive_rel(tail, factored_edges)
                total += first.r * self.recursive_rel(tail, factored_edges  + [first])

                return total
            elif is_connected(factored_edges):
                return 1
            else:
                return 0

