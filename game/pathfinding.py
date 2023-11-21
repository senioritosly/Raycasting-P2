from collections import deque

class PathFinding:
    def __init__(self, game):
        self.game = game
        self.map = game.map.mini_map
        self.ways = [-1,0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, 1], [-1, 1]
        self.graph = {}
        self.get_graph()

    def get_path(self, start, goal):
        self.visited = self.bfs(start, goal, self.graph)
        path = [goal]
        step = self.visited.get(goal, start)

        while step and step != start:
            path.append(step)
            step = self.visited[step]
        return path[-1]

    def bfs(self, start, goal, graph):
        queue = deque([start])
        visited = {start: None}
        while queue:
            current = queue.popleft()
            if current == goal:
                break
            next_nodes = graph[current]

            for node in next_nodes:
                if node not in visited and node not in self.game.object_handler.npc_positions:
                    queue.append(node)
                    visited[node] = current
        return visited

    def get_neighbours(self, x, y):
        return [(x + dx, y + dy) for dx, dy in self.ways if (x + dx, y + dy) not in self.game.map.world_map]

    def get_graph(self):
        for y, row in enumerate(self.map):
            for x, tile in enumerate(row):
                if not tile:
                    self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_neighbours(x, y)