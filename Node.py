class Node:
    def __init__(self, state, parent, action, depth, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth
        self.path_cost = path_cost
        self.evaluation_cost = 0
    
    def total_cost(self):
        return self.path_cost + self.evaluation_cost
    
    def state_hash(self):
        return str(self.state)