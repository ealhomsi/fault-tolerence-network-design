# The input file is in the format:
# Number of cities: A B C D ...(N cities)
# Cost/Reliability matrix: A-B,A-C,A-D...B-C,B-D...C-D....(N(N-1)/2)

'''
usage: main.py [-h] [-f FILE_PATH] -r RELIABILITY_GOAL -c COST_CONSTRAINT

optional arguments:
  -h, --help            show this help message and exit
  -f FILE_PATH, --input-file FILE_PATH
                        InputFile to work on
  -r RELIABILITY_GOAL, --reliability-goal RELIABILITY_GOAL
                        the reliability goal of the network
  -c COST_CONSTRAINT, --cost-constraint COST_CONSTRAINT
                        the cost constraint of the network
'''

from mst import MST
from edge_generator import EdgeGenerator
from argparse import ArgumentParser
from rel_calculator import RelCalculator

class Main:
    @staticmethod
    def parseArgs():
        parser = ArgumentParser()
        parser.add_argument('-f', '--input-file', action='store', type=str,
                            dest='file_path', help='InputFile to work on', default='input.txt')
        parser.add_argument('-r', '--reliability-goal', action='store', dest='reliability_goal',
                            help='the reliability goal of the network', type=float, required=True)
        parser.add_argument('-c', '--cost-constraint', action='store', dest='cost_constraint',
                            help='the cost constraint of the network', type=float, required=True)
        return parser.parse_args()

    @staticmethod
    def show_mst(cities, edges):
        # generate the limits of the problem
        mst = MST(cities, edges)
        min_cost_tree, min_cost = mst.min_cost_tree()
        max_reliability_tree, max_rel = mst.max_rel_tree()

        # print trees for debugging
        print("min cost tree")
        print(min_cost_tree)
        print("min cost tree value is {}".format(min_cost))
        print('\n')

        print("max reliability tree")
        print(max_reliability_tree)
        print("max reliability tree value is {}".format(max_rel))
        print('\n')

        return min_cost_tree
    
    @staticmethod
    def optimal_solution(cities, edges, cost_constraint, reliability_goal, initial_solution):
        def attemptAcceptance(cost, costgoal, rel, relgoal):
            return (cost <= costgoal and rel >= relgoal)

        def sumCost(edges):
            return sum(map(lambda x: x.c, edges))

        # start from min_cost tree and build up
        rel_calculator = RelCalculator(cities)

        graph = initial_solution
        cost = sumCost(graph)
        rel = rel_calculator.recursive_rel(graph, [])
        while(cost <= cost_constraint and rel < reliability_goal and len(graph) < len(cities)):
            unadded_edges = [item for item in edges if item not in graph]

            solutions_list = []
            for unadded_edge in unadded_edges:
                sol_cost = sumCost(graph + [unadded_edge])
                if(sol_cost < cost_constraint):
                    solutions_list.append((
                        sol_cost,
                        rel_calculator.recursive_rel(graph + [unadded_edge], []),
                        unadded_edge
                        ))
            
            best_candidate = None
            best_ratio = None
            for c,r,e in solutions_list:
                if (best_candidate == None or (r/c) > best_ratio):
                    best_ratio = r /c
                    best_candidate = e

            if best_candidate == None:
                break
            else:
                graph.append(best_candidate)
                cost = sumCost(graph)
                rel = rel_calculator.recursive_rel(graph, [])


        if(attemptAcceptance(cost, cost_constraint, rel, reliability_goal)):
            print("Solution was found with reliability of {} and cost of {}".format(rel, cost))
            print("Solution: \n")
            print(graph)
        else:
            print("The problem is unfeasable and no solution was found")
    
    @staticmethod
    def printInput(cities, edges):
        # print cities and edges for debugging purposes
        print("list of cities and edges")
        print(cities)
        print(edges)
        print('\n')

    @staticmethod
    def main():
        result = None

        try:
            result = Main.parseArgs()
        except Exception as e:
            print(e)
            exit()

        file_path = result.file_path
        reliability_goal = result.reliability_goal + 1e-10 # add epsilon for numerical stability
        cost_constraint = result.cost_constraint + 1e-10

        cities, edges = EdgeGenerator.generate(file_path)

        # show Input
        Main.printInput(cities, edges)

        # show MST calculations
        initial_solution = Main.show_mst(cities, edges)

        # find the optimal solution
        Main.optimal_solution(cities, edges, cost_constraint, reliability_goal, initial_solution)
        

if __name__ == "__main__":
    Main.main()
