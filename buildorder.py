#This program runs to find the build order of projects, with dependencies,
#using bfs
def build_order(proj, dep):
    orig_len = len(proj)
    #build order list
    bo = []
    root = list(proj)
    #find the starting proj that has no dependencies
    for pair in dep:
        if pair[1] in root:
            root.remove(pair[1])
    #if there are no project with no dependencies, return False
    if len(root) == 0:
        return False
    #start bfs to traverse through the graph, using the starting node as the
    #starting point
    #queue used in bfs
    q = []

    for node in root:
        q.append(node)
        proj.remove(node)
        while(len(q)!=0):
            r = q.pop(0)
            bo.append(r)
            #call a function to find the children of a node
            children = find_children(r, dep, proj)
            for child in children:
                q.append(child)

    if len(bo) == orig_len:
        return bo
    else:
        return False

def find_children(parent, dep, proj):
    children = []
    #store the found pairs
    children_pair = []
    for pair in dep:
        if parent == pair[0] and pair[1] in proj:
            child = pair[1]
            children_pair.append(pair)
            only_parent = True
            #double check to see if children has another dependencies beside
            #parent
            for t in dep:
                if child == t[1] and parent != t[0]:
                    only_parent = False
            #only return the child if it has only 1 parent
            if only_parent == True:
                children.append(child)
                proj.remove(child)
    #remove each found pair, even if we don't include the child in this
    #iteration because it can always be built later because there exist a pair
    #with that child and a different parent
    for pair in children_pair:
        dep.remove(pair)
    return children

def main():
    #simple test case
    proj = ['a', 'b', 'c', 'd', 'e', 'f']
    dep = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]

    print(build_order(proj, dep))

if __name__ == "__main__":
    main()
