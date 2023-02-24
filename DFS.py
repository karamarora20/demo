from Equation import Expression
import regex as re
class graph:
    
    def __init__(self,n):
        self.vertices=[i for i in range(n)]
        self.edges={}

    def add_edge(self,node,child,wt):
        if node in self.edges.keys():
            self.edges[node].append([child,wt])
        else:
            self.edges[node]=[[child,wt]]
    
    def print_g(self):
        for node,children in self.edges.items():
            
                for child in children:
                    print(f'{node} => {child[0]} (wt=> {child[1]})')
    def dfs(self,node,visited=set()):
        global goal
        if visited is None:
            visited=set()
        visited.add(node)
        if node== goal:
            print(f'Goal found and the path is {visited}')
        else:
            for next in self.edges[node]:
                # n,w= next.items()
                if next[0] not in visited:
                    self.dfs(next[0],visited)
    
    def dfs_wt(self,node,visited=set()):
        global goal
        if visited is None:
            visited=set()
        visited.add(node)
        if node== goal:
            print(f'Goal found and the path is {visited}')
        else:
            for next in self.edges[node]:
                
                if next[0] not in visited:
                    self.dfs_wt(next[0],visited)
    
    
    def create_graph(self):
        for k in range(n):
            for j in range(n):
                if adjacency_mat[k][j]==1:
                    w= int(input(f' enter wt for edge {k}=>{j}: '))
                    self.add_edge(k,j,w)     
        
            
            
        
        
    
    
                
if __name__=='__main__':
    n=int(input('number of vertices: '))
    g= graph(n)
    adjacency_mat=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        edges=list(map(int,input(f'enter the children for node {i}: ').split(',')))
        for j in edges:
            w=input(f'enter the constraint for edge {i}=>{j}: ')
            w=re.split('\W',w)
            print(w)
            
            g.add_edge(i,j,w)
        # row= list(map(int,input(f'enter the values for node {i}: ').split(',')))
        # adjacency_mat.append(row)
        
    
    goal= int(input('enter goal: '))            
    g.create_graph()
            
    # g.print_g()
    g.dfs(0)
    

    
    
            
            
            
            
        