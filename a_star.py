import heapq

import numpy as np

from utils.h_functions import heuristic_functions
from utils.map_init import CellType, create_map


class AStarPathfinder:
    def __init__(self, size, obstacle_ratio, heuristic="manhattan"):
        self.size = size
        self.initial_map = create_map(size, int(size * size * obstacle_ratio))
        self.map = None
        self.heuristic = heuristic_functions[heuristic]
        self.g_scores = np.full((size, size), np.inf)
        self.parents = np.full((size, size, 2), -1, dtype=int)
        self.f_minheap = []
        self.directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        self.start = tuple(np.argwhere(self.initial_map == CellType.START)[0])
        self.goal = tuple(np.argwhere(self.initial_map == CellType.END)[0])

    def is_valid(self, y, x, from_y=None, from_x=None):
        # 基本的有效性检查
        if not (0 <= y < self.size and 0 <= x < self.size):
            return False
        if self.initial_map[y, x] == CellType.OBSTACLE:
            return False

        if from_y is None or from_x is None:
            return True

        # 检查是否是对角线移动
        if abs(y - from_y) == 1 and abs(x - from_x) == 1:
            # 检查两个相邻的格子是否都不是障碍物
            if (
                self.initial_map[from_y, x] == CellType.OBSTACLE
                or self.initial_map[y, from_x] == CellType.OBSTACLE
            ):
                return False

        return True

    def get_path_cost(self, current, neighbor):
        dx = abs(current[0] - neighbor[0])
        dy = abs(current[1] - neighbor[1])
        return 14 if dx == 1 and dy == 1 else 10

    def find_path(self):
        # 复制初始地图
        self.map = self.initial_map.copy()

        self.g_scores.fill(np.inf)
        self.parents.fill(-1)
        self.f_minheap = []

        self.g_scores[self.start] = 0
        f_score = self.heuristic(self.start, self.goal)
        heapq.heappush(self.f_minheap, (f_score, self.start))

        while self.f_minheap:
            current_f, current = heapq.heappop(self.f_minheap)

            if current == self.goal:
                self.reconstruct_path()
                return self.map

            for direction in self.directions:
                neighbor = (current[0] + direction[0], current[1] + direction[1])
                if not self.is_valid(neighbor[0], neighbor[1], current[0], current[1]):
                    continue

                tentative_g = self.g_scores[current] + self.get_path_cost(
                    current, neighbor
                )

                if tentative_g < self.g_scores[neighbor]:
                    self.parents[neighbor] = current
                    self.g_scores[neighbor] = tentative_g
                    h = self.heuristic(neighbor, self.goal)
                    f_score = tentative_g + h
                    heapq.heappush(self.f_minheap, (f_score, neighbor))

                    if self.map[neighbor] == CellType.EMPTY:
                        self.map[neighbor] = CellType.SEARCHED

        return None  # 没有找到路径

    def reconstruct_path(self):
        current = self.goal
        while current != self.start:
            if self.map[current] == CellType.SEARCHED:
                self.map[current] = CellType.PATH
            current = tuple(self.parents[current])

    def get_initial_map(self):
        return self.initial_map

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic_functions[heuristic]

    def get_total_cost(self):
        return self.g_scores[self.goal]
