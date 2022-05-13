from Node import Node
from Schedule import Schedule

class SearchAlgorithm:
    def __init__(self, initial_state, expand_node, goal_test):
        self.nodes = [Node(initial_state, None, None, 1, 1)]
        self.expand_node = expand_node
        self.goal_test = goal_test
        self.hashes = {self.nodes[0].state_hash: self.nodes[0]}
        self.schedule = Schedule()
        self.scheduling_function(self.expand_node(self.nodes[0]))
    
    def scheduling_function(self, nodes):
        raise NotImplementedError
    
    def find_path(self):
        i = 1
        print(f"No.\tState\tDepth\tCost")
        while not self.schedule.is_empty():
            node = self.schedule.remove_front()
            print(f"{i}\t{node.state}\t{node.depth}\t{node.path_cost}")

            if self.goal_test(node):
                return self.solution(node), node
            expanded_nodes = [new_node for new_node in self.expand_node(node) if new_node.state_hash not in self.hashes]
            self.scheduling_function(expanded_nodes)

            i += 1
        
        return False, None

    def solution(self, node):
        order = []

        while node.parent is not None:
            order.append(node.action)
            node = node.parent
        
        order = order[::-1]

        return order