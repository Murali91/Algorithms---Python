import sys
class Graph:
    
    def __init__(self,*args):
        self.nodes = list(args)
        self.node_count = len(self.nodes)
        self.edges = dict.fromkeys(args)
        
    
    def path(self,src,dest,cost):
        if not self.edges[src]:
            self.edges[src]={}
        self.edges[src][dest]=cost
    
    def depth_first_search(self,start_node):
        self.visited_stack = []
        self.visited_dfs = set()
        self.__dfs_helper(start_node)

    
    def __neighbor_check(self,current):
        for node in self.edges[current].keys():
            if not node in self.visited_dfs:
                return True
        return False
                
    
    def __dfs_helper(self,current):
        if len(self.visited_dfs)<self.node_count:
            self.visited_dfs.add(current)
            self.visited_stack.append(current)
            print "Visited Nodes:"+current
            if self.edges.get(current,None) and self.__neighbor_check(current):
                low = sys.maxint
                for key,value in self.edges[current].iteritems():
                    if not key in self.visited_dfs:
                        low = min(low,value)             
                        if value == low:
                            low_key = key
                self.__dfs_helper(low_key)
            elif self.visited_stack:
                self.visited_stack.pop()
                self.__dfs_helper(self.visited_stack.pop())

        else:
            print "Node traversal completed"
             
    def __bfs_helper(self,current):
        self.visited_bfs.add(current)
        print "Visited Nodes:"+current
        if len(self.visited_bfs)<self.node_count:
            if self.edges[current]:
                for key in self.edges[current].keys():
                    self.visited_queue.append(key)
            self.__bfs_helper(self.visited_queue.pop(0))
        else:
            print "Node traversal completed"
    
    def breadth_first_search(self,start_node):
        self.visited_queue = []
        self.visited_bfs = set()
        self.__bfs_helper(start_node)
        
