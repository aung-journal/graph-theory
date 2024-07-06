import time
start_time = time.time()
def all_topological_sorts(graph):
    #Step 0: find the degree of a node
    def calculate_in_degree(graph):
        in_degree = {node: 0 for node in graph}
        
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1
        
        return in_degree
    # Step 1: Initialize data structures
    in_degree = calculate_in_degree(graph)
    zero_in_degree_nodes = [node for node in graph if in_degree[node] == 0]
    result = []
    
    # Step 2: Backtracking function
    def backtrack(order):
        if len(order) == len(graph):
            result.append(order.copy())  # Found a valid topological ordering
            return
        
        for node in zero_in_degree_nodes:
            # Temporarily remove the node and update in-degrees
            order.append(node)
            zero_in_degree_nodes.remove(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_in_degree_nodes.append(neighbor)
            
            # Recursively backtrack
            backtrack(order)
            
            # Backtrack: restore previous state
            order.pop()
            zero_in_degree_nodes.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] += 1

    # Step 3: Start backtracking
    backtrack([])
    
    return result

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

#This is very slow and won't work
all_orders = all_topological_sorts(graph)
for order in all_orders:
    print(order)

end_time = time.time()
print("--- {} seconds ---".format(end_time - start_time))
