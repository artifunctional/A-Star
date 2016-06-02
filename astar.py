#!usr/bin/env python

from  Queue import PriorityQueue

class State(object):
    """docstring for State"""
    def __init__(self, value, parent,
                start = 0, goal = 0):
        self.children = []
        self.parent = parent
        self.value = value
        self.dist = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal
    
    def get_dist(self):
        pass
    def create_children(self):
        pass

class StateString(State):
    """docstring for StateString"""
    def __init__(self, value, parent,
                start = 0, goal = 0):
        super(StateString, self).__init__(
                value, parent,
                start, goal)
        self.dist = self.get_dist()

    def get_dist(self):
        if self.value == self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter = self.goal[i]
            dist += abs(i - self.value.index(letter))
        return dist

    def create_children(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val = self.value
                val = val[:i] + val[i+1] + val[i] + val[i+2:]
                child = StateString(val, self)
                self.children.append(child)

class AStarSolver(object):
    """docstring for AStarSolver"""
    def __init__(self, start, goal):
        self.path = []
        self.visited_queue = []
        self.priority_queue = PriorityQueue()
        self.start = start
        self.goal = goal

    def solve(self):
        start_state = StateString(
                        self.start,
                        0,
                        self.start,
                        self.goal
                        )
        self.priority_queue.put((0,start_state))
        while not self.path and self.priority_queue.qsize():
            closest_child = self.priority_queue.get()[1]
            closest_child.create_children()
            self.visited_queue.append(closest_child.value)
            for child in closest_child.children:
                if child.value not in self.visited_queue:
                    if not child.dist:
                        self.path = child.path
                        break
                    self.priority_queue.put((child.dist, child))
        if not self.path:
            print "Could not reach the goal: " + self.goal
        return self.path

# Main

if __name__ == "__main__":
    start = "123456789"
    goal = "987654321"
    print "solving ..."
    a= AStarSolver(start, goal)
    a.solve()
    for i in xrange(len(a.path)):
        print "(%d) " %i + a.path[i]
