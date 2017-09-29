import heapq
from collections import defaultdict

# define chessboard parameters
BOARD_SIZE      = 8
BOARD_MOVEMENTS = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                   (2, 1), (2, -1), (-2, 1), (-2, -1)]

class Node:
    def __init__(self, x, y, distance=0):
        self.x = x
        self.y = y
        self.distance = distance

    def __hash__(self):
        return hash(tuple(self))

    def __iter__(self):
        for i in [self.x, self.y]:
            yield i

    def __eq__(self, node):
        return self.x == node.x and self.y == node.y

    def __lt__(self, other):
        return self.x < node.x or (self.x == node.x and self.y < node.y)

    def __str__(self):
        return "<Node (x=%d, y=%d, d=%.02f)>" % (self.x, self.y, self.distance)

    def __repr__(self):
        return self.__str__()

class Board:
    def __init__(self, size, movements):
        self.size = size
        self.movements = movements

    def node(self, position):
        """ Generate Node for given position """
        return Node(int(position % self.size) + 1, int(position / self.size) + 1)

    def valid(self, x, y):
        return True if x >= 0 < self.size and y >= 0 < self.size else False

    def distance(self, start, end):
        """ Find shortest distance using BFS """
        queue = []
        queue.append(start)
        visited = {}

        # run until queue is empty
        while queue:
            # grab first node in queue
            node = queue.pop(0)

            # return when destination is reached
            if node == end:
                return node.distance

            # process nodes that have not been visited
            if node not in visited:
                # mark node as visited
                visited[node] = True

                # validate piece movement
                for offset in self.movements:
                    x, y = list(tuple(x + y for x, y in zip(tuple(node), offset)))

                    # queue valid moves only
                    if self.valid(x, y):
                        queue.append(Node(x, y, node.distance + 1))

        return float('inf')

def answer(src, dest):
    # create chessboard graph
    chessboard = Board(size = BOARD_SIZE, movements = BOARD_MOVEMENTS)

    # create coordinates
    start = chessboard.node(src)
    end = chessboard.node(dest)

    # calculate distance between given positions
    distance = chessboard.distance(start, end)

    return distance
