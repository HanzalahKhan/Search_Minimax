from utils import get_neighbours
from collections import deque

def Bfs(Grid, START, END, size):
    frontier = deque([START])
    exploredset = set()
    exploredset.add(START)
    finalpath = {}
    exploredpaths = []

    while frontier:
        current = frontier.popleft()
        exploredpaths.append(current)

        if current == END:
            way = []
            while current != START:
                way.append(current)
                current = finalpath[current]
            way.append(START)
            way.reverse()
            return way, exploredpaths

        children = get_neighbours(current, size)
        for child in children:
            x, y = child
    
            if child not in exploredset and Grid[x][y] != 1:
                frontier.append(child)
                exploredset.add(child)
                finalpath[child] = current

    return [], exploredpaths


