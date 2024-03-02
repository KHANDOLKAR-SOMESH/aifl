from collections import deque

def add_edge(adjlist, node1, node2, weight): #fun 2 add edge
    adjlist.setdefault(node1, []).append((node2, weight))
    adjlist.setdefault(node2, []).append((node1, weight))

def set_heuristic(heuristic, node, value):
    heuristic[node] = value

def get_neighbors(adjlist, v):
    return adjlist[v]

def h(heuristic, n):
    return heuristic[n]

def astar(adjlist, heuristic, start, stop):
    openlist = {start}
    closelist = set()
    cost = {start: 0}
    par = {start: start}
    while openlist:
        n = min(openlist, key=lambda x: cost[x] + h(heuristic, x))
        if n == stop:
            path = []
            while n != start:
                path.append(n)
                n = par[n]
            path.append(start)
            print('Path found:', ' -> '.join(path[::-1]))
            return path
        for m, weight in get_neighbors(adjlist, n):
            new_cost = cost[n] + weight
            if m not in openlist and m not in closelist:
                openlist.add(m)
                cost[m], par[m] = new_cost, n
            elif new_cost < cost[m]:
                cost[m], par[m] = new_cost, n
                if m in closelist:
                    closelist.remove(m)
                    openlist.add(m)
        openlist.remove(n)
        closelist.add(n)
    print('path is not present')

adjlist = {}
heuristic = {}

num_edges = int(input("ebter the number of edges: "))
print("Enter edges in the format |node1 node2 weight|:")
for i in range(num_edges):
    node1, node2, weight = input().split()
    add_edge(adjlist, node1, node2, int(weight))
print("Enter heuristic values in the format 'node value', or 'end' to exit:")
while True:
    heuristic_input = input().split()
    if heuristic_input[0] == 'end':
        break
    node, value = heuristic_input

    set_heuristic(heuristic, node, int(value))

start_node = input("Enter start node: ")

end_node = input("Enter end node: ")

astar(adjlist, heuristic, start_node, end_node)
