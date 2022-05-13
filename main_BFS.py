from BreadthFirstSearch import BreadthFirstSearch
from TransportationProblem import TransportationProblem

problem = TransportationProblem(7)
dfs = BreadthFirstSearch(1, problem.succ_and_cost, problem.is_end)
print(dfs.find_path())