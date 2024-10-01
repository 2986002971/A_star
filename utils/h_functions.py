import numpy as np


def manhattan_distance(a, b):
    return 10 * (abs(a[0] - b[0]) + abs(a[1] - b[1]))


def euclidean_distance(a, b):
    return 10 * np.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def chebyshev_distance(a, b):
    return 10 * max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def zero_heuristic(a, b):
    return 0


def greedy_best_first(a, b):
    """
    贪心最佳优先搜索的估值函数
    这里使用曼哈顿距离作为估值，并乘以一个较大的系数来确保贪心行为
    """
    return 1000 * manhattan_distance(a, b)


# 创建一个字典来映射算法名称和对应的估值函数
heuristic_functions = {
    "manhattan": manhattan_distance,
    "greedy": greedy_best_first,
    "dijkstra": zero_heuristic,
    "euclidean": euclidean_distance,
    "chebyshev": chebyshev_distance,
}
