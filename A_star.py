from utils import get_neighbours
import heapq

def heuristic(cell1, cell2):
    a, b = cell1
    c, d = cell2

    return abs(d - b) + abs(c - a)

def A_star(Grid, START, END, size):

    sortedbycost = []
    heapq.heappush(sortedbycost, (0, START))
    
    nodewithcost = {START:0}
    
    exploredset = set()
    
    finalpath = {}
    
    exploredpaths = []
    
    while sortedbycost:
        _ , current = heapq.heappop(sortedbycost)
        exploredpaths.append(current)
        
        if current == END:
            way = []
            
            while current in finalpath:
                way.append(current)
                current = finalpath[current]
            way.append(START)
            way.reverse()
            return way, exploredpaths
                
        exploredset.add(START)
        
        children = get_neighbours(current, size)
        
        for child in children:
            x, y = child
            
            if child not in exploredset and Grid[x][y] != 1:
                newcost = nodewithcost[current] + Grid[x][y]
                
                if child not in nodewithcost or newcost < nodewithcost[child]:
                    nodewithcost[child] = newcost
                    totalcost = newcost + heuristic(child, END)
                    heapq.heappush(sortedbycost, (totalcost, child))
                    finalpath[child] = current
                
                

    return [], exploredpaths