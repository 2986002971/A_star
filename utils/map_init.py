from enum import IntEnum

import numpy as np


class CellType(IntEnum):
    """定义地图上不同类型的方格"""

    EMPTY = 0  # 可用路径
    OBSTACLE = 1  # 障碍物
    SEARCHED = 2  # 已搜索的路径
    PATH = 3  # 选定的路径
    START = 4  # 起点
    END = 5  # 终点


def create_map(size, obstacle_num):
    """
    创建一个用于A*算法的地图

    参数:
    size (int): 地图的大小 (size x size)
    obstacle_num (int): 障碍物的数量

    返回:
    numpy.ndarray: 生成的地图, 使用CellType枚举值表示不同类型的方格
    """
    # 创建一个全为EMPTY的二维数组
    map_array = np.full((size, size), CellType.EMPTY, dtype=int)

    # 随机放置障碍物
    obstacles = np.random.choice(size * size, obstacle_num, replace=False)
    map_array.flat[obstacles] = CellType.OBSTACLE

    # 随机选择起点和终点
    while True:
        start_x = np.random.randint(size)
        start_y = np.random.randint(size)
        end_x = np.random.randint(size)
        end_y = np.random.randint(size)
        if (
            map_array[start_x, start_y] == CellType.OBSTACLE
            or map_array[end_x, end_y] == CellType.OBSTACLE
        ):
            continue
        if start_x == end_x and start_y == end_y:
            continue
        map_array[start_x, start_y] = CellType.START
        map_array[end_x, end_y] = CellType.END
        break

    return map_array
