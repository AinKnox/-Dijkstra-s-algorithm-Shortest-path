import heapq

# Функция Дейкстры для нахождения кратчайшего пути в графе
def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_node == end:
            break

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph[current_node]:
            distance = current_distance + 1

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    path = path[::-1]

    return path, distances[end]

graph = {
    1: [2],
    2: [1, 3, 4, 6],
    3: [2, 4, 5],
    4: [2, 3, 5, 6],
    5: [3, 4, 6],
    6: [2, 4, 5]
}

# Нахождение кратчайшего пути от вершины 1 до 6 в обновленном графе
path, distance = dijkstra(graph, 1, 6)

log_content = f"Кратчайший путь из вершины 1 в вершину 6: {path}\nРасстояние: {distance}\n"

log_file_path = "shortest_path.txt"
with open(log_file_path, 'w') as log_file:
    log_file.write(log_content)

print(f"Лог сохранен в файл: {log_file_path}")
