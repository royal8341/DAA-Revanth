import heapq

def kClosest(points, k):
    heap = [(-((x**2 + y**2)**0.5), x, y) for x, y in points]
    heapq.heapify(heap)
    result = []
    for _ in range(k):
        dist, x, y = heapq.heappop(heap)
        result.append([x,y])
    return result


points = [[1, 3], [-2, 2]]
k = 1
print(kClosest(points, k))  
