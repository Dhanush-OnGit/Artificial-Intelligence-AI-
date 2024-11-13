gragh = {
    'a':['b','c'],
    'b':['a','c','d'],
    'c':['a','b','d'],
    'd':['b','c']
}
visited = []
queue = []
def bfs(visited,gragh,startnode,goalnode):
    flag =0
    visited.append(startnode)
    queue.append(startnode)
    while queue:
        m = queue.pop(0)
        for neibour in gragh[m]:
            if flag == 0:
                if neibour not in visited:
                    visited.append(neibour)
                    queue.append(neibour)
                    print("visited",visited)
                    if neibour == goalnode:
                        print("goal is reached")
                        print("the path is :",visited)
                        flag =1
    if flag == 0:
        print("goal is not reached")
print("BFS")  
bfs(visited,gragh,'a','d')              