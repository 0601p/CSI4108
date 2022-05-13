from SearchAlgorithm import SearchAlgorithm

class BreadthFirstSearch(SearchAlgorithm):
    def __init__(self, initial_state, expand_node, goal_test):
        SearchAlgorithm.__init__(self, initial_state, expand_node, goal_test)
    
    def scheduling_function(self, nodes):
        self.schedule.items.extend(nodes)