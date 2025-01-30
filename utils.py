def get_neighbours(node, size):
    x, y = node
    neighbours = []
    if x > 0: neighbours.append((x - 1, y))  
    if x < size - 1: neighbours.append((x + 1, y)) 
    if y > 0: neighbours.append((x, y - 1))  
    if y < size - 1: neighbours.append((x, y + 1)) 
    return neighbours