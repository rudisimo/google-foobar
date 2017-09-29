# define chessboard knight movements
BOARD_SIZE = 8

def calculate_possible_moves():
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    column = [-1, 1, 1, -1, 2, -2, 2, -2]
    deltas = zip(row, column)

    return [
        [6, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 6],
        [5, 4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4, 5],
        [4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4],
        [5, 4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4, 5],
        [4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4],
        [5, 4, 3, 2, 3, 4, 1, 2, 1, 4, 3, 2, 3, 4, 5],
        [4, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 4],
        [5, 4, 3, 2, 3, 2, 3, 0, 3, 2, 3, 2, 3, 4, 5],
        [4, 3, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3, 4, 3, 4],
        [5, 4, 3, 2, 3, 4, 1, 2, 1, 4, 3, 2, 3, 4, 5],
        [4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4],
        [5, 4, 3, 4, 3, 2, 3, 2, 3, 2, 3, 4, 3, 4, 5],
        [4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4],
        [5, 4, 5, 4, 3, 4, 3, 4, 3, 4, 3, 4, 5, 4, 5],
        [6, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 6]
    ]

def calculate_possible_moves(start, finish):
    board = [[0 for y in xrange(BOARD_SIZE)] for x in xrange(BOARD_SIZE)]
    #print(board)

    queue = [start]
    offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
               (2, 1), (2, -1), (-2, 1), (-2, -1)]

    while len(queue):
        current = queue.pop(0)
        if current == finish:
            return 

        for offset in offsets:
            step = tuple(x + y for x, y in zip(current, offset))
            if step[0] > 0 and step[0] < finish:
                continue
            if step[1] > finish[1]:
                continue
            if step[0] < 1:
                continue
            if step[1] < 1:
                continue
            if 

        #    if 0 < move[0] and 0 < move[1] < 8:
        #        yield move

def calculate_position_coordinates(position):
    return int(position % BOARD_SIZE) + 1, int(int(position / BOARD_SIZE) + 1)

def answer(src, dest):
    distance = {}
    position = {}

    start = calculate_position_coordinates(src)
    finish = calculate_position_coordinates(dest)
    print(start)
    print(finish)

    queue = [start]

    moves = calculate_possible_moves(start, finish)

    print(moves)

    maximum = (7, 7)
    distance = tuple(x - y for x, y in zip(start, finish))
    position = tuple(x + y for x, y in zip(distance, maximum))

    return moves[position[0]][position[1]]
