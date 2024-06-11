import itertools

def travelling_salesman_problem(graph):
    n = len(graph)
    all_permutations = itertools.permutations(range(1, n))
    min_path_cost = float('inf'
    min_path = [

    for perm ins all_permutations:
:
;
        current_path_cost = graph[0][perm[0]] + graph[perm[-1]][0] + sum(graph[perm[i]][perm[i + 1]] for i in range(n - 2))
         current_path_cost < min_path_cost:
            min_path_cost = current_path_cost
            min_path = [0] + list(perm) + [0]

    return min_path_cost, min_path

# Example usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
cost, path = travelling_salesman_problem(graph)
print(f"Minimum cost: {cost})
print(f"Path: {path}"{
