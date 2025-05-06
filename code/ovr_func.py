import pulp

def create_array(arr):
    n = len(arr)
    prob = pulp.LpProblem('find_max_index',sense=pulp.LpMaximize)
    tpe = [pulp.LpVariable(name=f'x{i}',cat="Binary") for i in range(n)]
    
    prob += (pulp.lpSum(tpe) == 1)
    sum = pulp.lpSum([tpe[i] * arr[i] for i in range(n)])
    prob += sum
    
    prob.solve()
    
    return tpe
    
    
        
        

    
def main():
    arr = [1,2,7,3,2]
    t = create_array(arr)
    for a in t:
        print(a.varValue)
    
if __name__ == "__main__":
    main()
    
    
    
    
        
            