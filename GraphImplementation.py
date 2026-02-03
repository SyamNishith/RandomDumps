def add_node(n):
    global node_count
    if n in nodes:
        print(n,"is already present in the graph:")
    else:
        node_count=node_count+1
        nodes.append(n)#append new node to the nodes list
        for n in graph:#append new column to the graph
            n.append(0)
        temp=[]
        for i in range(node_count):   #append new row to the graph
            temp.append(0)
        graph.append(temp)
def add_edge(v1,v2): #for unweighted graph
    #if u want weighted graph then u can add cost parameter to the function
    if v1 not in nodes:
        print(v1,"not present in the graph:")
    elif v2 not in nodes:
        print(v2,"not present in the graph:")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1 # for undirected graph
        graph[index2][index1]=1 # for undirected graph
        #if u want directed graph then second statement is not necessary
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(graph[i][j],end=" ")
        print()
def delete_node(v):
    global node_count
    if v not in nodes:
        print(v,"is not present in the graph cannot perform delete operation")
    else:
        index1=nodes.index(v)
        node_count=node_count-1
        nodes.remove(v)
        graph.pop(index1)
        for i in graph:
            i.pop(index1)
def delete_edge(v1,v2):
    if v1 not in nodes:
        print(v1,"not present in the graph")
    elif v2 not in nodes:
        print(v2,"not present in the graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0
nodes=[]
graph=[]
node_count=0
print("before adding node:")
print(nodes)
print(graph)
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
print("after adding node:")
print(nodes)
add_edge("A","B")
add_edge("A","C")
add_edge("D","C")
add_edge("E","D")
print(graph)
delete_node("C")
delete_edge("E","D")
print(graph)
print_graph()

