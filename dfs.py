gragh = {
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited =[]
def dfs(visited,gragh,startnode,goalnode):
    flag = 0
    if startnode not in visited:
        visited.append(startnode)
        if startnode == goalnode:
            print("Goal is reached")
            print("the path is : ",visited)
        elif flag == 0:
            for neibour in gragh[startnode]:
                dfs(visited,gragh,neibour,goalnode)
    elif flag == 0:
        print("goal is not reached")
print("DFS")
dfs(visited,gragh,'5','7')