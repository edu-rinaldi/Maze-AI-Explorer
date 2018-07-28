from math import sqrt


def manhattan(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def euclidean(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def mapFromTo(x,a,b,c,d):
   return (x-a)/(b-a)*(d-c)+c


def sumTuple(t1,t2):
    return (t1[0]+t2[0], t1[1]+t2[1])


def pathfinding(start,goal,map):
    closedset = set()
    openset = set()
    openset.add(start)
    g_score = {start:0}
    camefrom = dict()
    h_score = {start:manhattan(start[1],start[0],goal[1],goal[0])}
    f_score = {start: h_score[start]}

    while len(openset)>0:
        x = min(openset, key=lambda coord: f_score[coord])
        if x == goal:
            return reconstruct_path(camefrom,goal)
        openset.remove(x)
        closedset.add(x)
        for y in neighbours(x, map):
            if y in closedset or map[y[0]][y[1]]!=(255,255,255):
                continue
            tentative_g_score = g_score[x] + 1
            if y not in openset:
                openset.add(y)
                tentative_is_better = True
            elif tentative_g_score < g_score[y]:
                tentative_is_better = True
            else: tentative_is_better = False
            if tentative_is_better:
                camefrom[y] = x
                g_score[y] = tentative_g_score
                h_score[y] = manhattan(y[1],y[0],goal[1],goal[0])
                f_score[y] = g_score[y] + h_score[y]
    return False


def neighbours(x, map):
    n = []
    offset = [(0,1),(1,0),(0,-1),(-1,0)]
    for c in offset:
        oy = x[0]+c[0]
        ox = x[1]+c[1]

        if 0<=ox<len(map[0]) and 0<=oy<len(map):
            n.append((oy,ox))
    return n


def reconstruct_path(camefrom,current_node):
    p = [current_node]
    while camefrom[current_node] in camefrom:
        current_node = camefrom[current_node]
        p.extend([current_node])
    return p



def reconstruct_path2(camefrom,current_node):
    if camefrom[current_node] in camefrom:
        p = reconstruct_path(camefrom,camefrom[current_node])
        p.extend([current_node])
        return p
    else:
        return [current_node]


{ (0,1): (1,2), (1,2):(2,1), }
