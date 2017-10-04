from collections import deque

# define space station parameters
WALL_POWER = 1

class Node:
    def __init__(self, x, y, power=0):
        self.x = x
        self.y = y
        self.power = power

    def __iter__(self):
        return iter([self.x, self.y])

    def __hash__(self):
        return hash(tuple(self))

    def __eq__(self, node):
        return self.x == node.x and self.y == node.y

    def __str__(self):
        return "({n.x}, {n.y})".format(n=self)

    def __repr__(self):
        return self.__str__()

class Router:
    def __init__(self, matrix, power):
        self.matrix = matrix
        self.power = power

        self.width = len(matrix[0])
        self.height = len(matrix)
        self.offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        self.visited = set()
        self.distances = {}

    def is_wall(self, x, y):
        return self.matrix[y][x] == 1

    def get_adjacent(self, node):
        for offset in self.offsets:
            x, y = list(tuple(u + v for u, v in zip((node.x, node.y), offset)))
            if self.width > x >= 0 and self.height > y >= 0:
                neighbor = Node(x, y, node.power)
                if self.is_wall(x, y):
                    if neighbor.power > 0:
                        neighbor.power -= 1
                        yield neighbor
                else:
                    yield neighbor

    def distance(self, start, end):
        # configure initial values
        self.distances[start] = 1
        start.power = self.power

        # configure queue
        queue = deque([])
        queue.append(start)

        while queue:
            # grab first node in queue
            current = queue.popleft()
            self.visited.add(current)

            # return distance when we reach our destination
            if current == end:
                return self.distances[current]

            # find all adjacent nodes
            for neighbor in self.get_adjacent(current):
                # process unvisited nodes only
                if neighbor not in self.visited:
                    self.distances[neighbor] = self.distances[current] + 1
                    queue.append(neighbor)

        return float('inf')

def answer(maze):
    # create space station router
    station = Router(maze, power=WALL_POWER)

    # create enter/exit coordinates
    enter = Node(0, 0)
    exit = Node(station.width-1, station.height-1)

    # calculate distance between given coordinates
    distance = station.distance(enter, exit)

    return distance
