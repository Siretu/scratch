# Some old DFS implementation

#d = {6:[5],5:[6,4],4:[1,2,3,5],1:[4,2],2:[4,1],3:[4]}
d = {6:[5],5:[6,4],4:[1,2,3,5],1:[4],2:[4],3:[4,7], 7: [3]}

def dfs(G,visited = set(), parent = -1, current = 1):
    visited.add(current)
    for x in G[current]:
        if x != parent:
            if x in visited:
                return False
            else:
                dfs(G,visited,current,x)
    return len(G.keys()) == len(visited)

print dfs(d)
print dfs(d)
