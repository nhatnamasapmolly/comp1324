nodes = [1, 6, 8, 7, 2, 3, 15, 4]

def independent_set(nodes):
    n = len(nodes) + 1
    optimal = [0] * n
    def optimal_arr(i):
        optimal[0] = 0
        optimal[1] = nodes[0]
        for i in range(2, len(nodes)+1):
            optimal[i] = max(optimal[i-1], optimal[i-2] + nodes[i-1])
            print(optimal[i])
    
    optimal_arr(nodes)
    i = len(nodes) -1 
    ans = []
    while i > 0:
        if optimal[i] > optimal[i-1]:
            ans.append(nodes[i-1])
            i -= 2
        else: 
            i -= 1
    return ans

print(independent_set(nodes))