def aStarAlgo(startNode,stopNode):
    openSet=set(startNode)
    closedSet=set()
    g={}
    parents={}
    g[startNode]=0
    parents[startNode]=startNode
    while(len(openSet)>0):
        n=None
        for v in openSet:
            if n==None or g[v]+heuristic(v)<g[n]+heuristic(n):
                n=v
        
        if n==stopNode or graphNode[n]==None:
            pass
        
        else:
            for (m,weight) in getNeighbors(n):
                if m not in openSet and m not in closedSet:
                    openSet.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        if m in closedSet:
                            closedSet.remove(m)
                            openSet.add(m)
        if n==None:
            print('path does not exist')
            return None
        if n==stopNode:
            path=[]
            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(startNode)
            path.reverse()
            print('path found {}'.format(path))
            return path
        openSet.remove(n)
        closedSet.add(n)
    print('Path does not exist')
    return None
def getNeighbors(n):
    if n in graphNode:
        return graphNode[n]
    else:
        return None
def heuristic(n):
    hDist={
        'A':11,'B':6,'C':99,'E':7,'D':1,'G':0
    }
    return hDist[n]
graphNode={
    'A':[('B',2),('E',3)],
    'B':[('A',2),('C',1)],
    'C':[('B',1)],
    'E':[('A',3),('D',6)],
    'D':[('E',6),('G',1)],
    'G':[('B',9),('D',1)]
}
aStarAlgo('A','G')
