class Schedule:
    def __init__(self):
        self.items = []
    
    def make_schedule(self, elements):
        self.items = elements
    
    def is_empty(self):
        return len(self.items) == 0
    
    def remove_front(self):
        return self.items.pop(0)
    
    def schedule_front(self, elements):
        self.items.insert(0, elements)
    
    def schedule_back(self, elements):
        self.items.extend(elements)