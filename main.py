
# The function takes a graph in adjacent matrix and the number of nodes or vertices the graph has
def mst(G,n):
    # array to show aquire the selected nodes
    selected_node = [0]*n

    # number of nodes in the graph
    total_nodes = n
    # the variable to help us track the number of nodes
    track_edge = 0
    # Selecting the starting node
    selected_node[0] = True

    while (track_edge < total_nodes - 1):
        # make an infinity number to be used in comparision with weights
        minimum = 999999999
        a = 0
        b = 0
        # two for loops to go through the adjacent matrix
        for m in range(total_nodes):
            if selected_node[m]:
                for n in range(total_nodes):
                    if (not selected_node[n]) and G[m][n]:
                        # not in selected and there is an edge
                        if minimum > G[m][n]:
                            minimum = G[m][n]
                            a = m
                            b = n
        # printing the way of the MST and the weight
        print(str(a)+"->"+str(b) +":" +str(G[a][b]))
        # label the node that it has been visited to avoid the coming back to it
        selected_node[b] = True
        track_edge += 1


# The graph
g=[[0, 10, 25, 0, 0 ,0, 0],
[10, 0, 0 ,28 ,0, 0, 0],
[25, 0, 0 ,0 ,24, 0, 22],
[0, 0, 0 ,0 ,14, 16, 0 ],
[0, 0, 24, 14, 0, 0, 18],
[0, 0, 0, 16, 0, 0, 12],
[0, 22, 0, 0, 18, 12, 0]]

#Calling the function
mst(g,7)