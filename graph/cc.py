class digraph:
    def __init__(self, infile=None):
        '''
        in: input stream with the format of one column start with -
        V: the number of vertices
        E: the number of edges
        edge 1: va vb
        edge 2: vi vj
        and so on
        '''
        self.adj = {}
        if infile is not None:
            with open(infile, 'r') as h:
                self.V = int(h.readline().strip())
                for i in range(self.V):
                    self.adj[i] = []
                self.E = int(h.readline().strip())
                for line in h:
                    edge = line.strip().split()
                    v, w = int(edge[0]), int(edge[1])
                    print(edge)
                    self.adj[v].append(w)            

        else:
            self.V = 0
            self.E = 0

    def addEdge(self, v, w):
        if v not in self.adj.keys():
            self.adj[v] = [w]
            self.V += 1
        else:
            self.adj[v].append(w)
        self.E += 1

    def adj(self, v):
        return self.adj[v]

class graph:
    def __init__(self, infile=None):
        self.adj = {}
        if infile is not None:
            with open(infile, 'r') as h:
                self.V = int(h.readline().strip())
                for i in range(self.V):
                    self.adj[i] = []
                self.E = int(h.readline().strip())
                for line in h:
                    edge = line.strip().split()
                    v, w = int(edge[0]), int(edge[1])
                    print(edge)
                    self.addEdge(v, w)

        else:
            print("Please build the graph as follows:")
            self.V = int(input('Number of vertices: '))
            for i in range(self.V):
                self.adj[i] = []
            self.E = int(input('Number of edges: '))
            for i in range(self.E):
                edge = input(f'Edge: {i}: ').split(',')
                v, w = int(edge[0]), int(edge[1])
                self.addEdge(v, w)


    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def adj(self, v):
        return self.adj[v]                    

class DepthFirstPaths:
    '''
    G: the input graph
    s: source of the graph
    '''
    def __init__(self, G, s):
        self.G = G
        self.s = s
        self.__marked = [False]*G.V
        self.__edgeTo = [-1]*G.V
        self.__stack = []
        self.preorder = []
        self.postorder = []
        self.dfs(s)

    def dfs(self, v):
        self.__marked[v] = True
        self.__stack.append(v)
        self.preorder.append(v)
        for w in self.G.adj[v]:
            if self.__marked[w]==False:
                self.dfs(w)
                self.__edgeTo[w] = v
        self.postorder.append(self.__stack.pop())
    

    def hasPathTo(self, v):
        return self.__marked[v]

    def pathTo(self, v):
        path = []
        while v!=-1:
            path.append(v)
            v = self.__edgeTo[v]
        return path
    
    def isConnected(self):
        '''
        check if all the non-zero degree are connected 
        '''
        self.__marked = [False]*self.G.V
        i = 0
        # take one non-zero degree vertex
        while i < self.G.V:
            if len(self.G.adj[i])>0:
                break
            i+=1
        # if no edge, return true
        if i==self.G.V:
            return True
        # and start to run dfs from that vertex
        self.dfs(i)
        
        # Check if all non-zero degree vertices are visited
        for i in range(self.G.V):
            if self.__marked[i]==False and len(self.G.adj[i])>0:
                return False
        return True

    def isEuler(self):
        '''
        0: not Eulerian
        1: has an Eularian path
        2: has an Eularian cycle 
        '''
        if self.isConnected() == False:
            return 0
        # Count the number of odd degree vertices
        odd = 0
        for i in range(self.G.V):
            if len(self.G.adj[i]) & 1:
                odd += 1
        # If count is more than 2, then graph is not Eulerian
        if odd > 2:
            return 0
        # If 2 -> semi; 0 -> Eularian; 1 impossible for undirected g
        if odd ==2:
            return 1
        if odd==0:
            return 2

        




class CC:
    '''
    connected component 
    '''
    def __init__(self, G):
        super().__init__()
        self.__marked = []
        self.__count = []
        self.G = G

    def build(self):
        self.G.V()
