from SearchProblem import SearchProblem
from Node import Node

class TransportationProblem(SearchProblem):
    def __init__(self, dest):
        self.dest = dest
    
    def is_end(self, state_node):
        if state_node.state == self.dest:
            return True
        return False
    
    def succ_and_cost(self, state_node):
        action_state_list = []
        if state_node.state + 1 <= self.dest:
            node_walk = Node(state_node.state + 1, state_node, 'walk', state_node.depth + 1, state_node.path_cost + 1)
            action_state_list.append(node_walk)
        if state_node.state * 2 <= self.dest:
            node_tram = Node(state_node.state * 2, state_node, 'tram', state_node.depth + 1, state_node.path_cost + 2)
            action_state_list.append(node_tram)
        return action_state_list