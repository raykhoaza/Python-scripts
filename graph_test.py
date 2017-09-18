from graph import Graph, Node, dfs, bfs, route

def main():
    G = Graph()

    node_0 = Node('0')
    G.nodes.append(node_0)

    node_1 = Node('1')
    G.nodes.append(node_1)

    node_2 = Node('2')
    G.nodes.append(node_2)

    node_3 = Node('3')
    G.nodes.append(node_3)

    node_4 = Node('4')
    G.nodes.append(node_4)

    node_5 = Node('5')
    G.nodes.append(node_5)

    node_0.children.append(node_1)
    node_0.children.append(node_4)
    node_0.children.append(node_5)

    node_1.children.append(node_3)
    node_1.children.append(node_4)

    node_2.children.append(node_1)

    node_3.children.append(node_2)
    node_3.children.append(node_4)

    #print (route(node_0, node_3))

    #dfs(node_0)

    #G.reset()
    #print(' ')

    #print(bfs(node_0))

if __name__ == "__main__":
    main()
