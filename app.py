import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from a_star import AStarPathfinder
from utils.map_init import CellType

# 设置页面标题
st.set_page_config(page_title="A* 路径查找可视化", layout="wide")

# 标题
st.title("A* 路径查找算法可视化")

# 初始化 session state
if "pathfinder" not in st.session_state:
    st.session_state.pathfinder = None

# 侧边栏参数设置
st.sidebar.header("参数设置")
size = st.sidebar.slider("地图大小", 10, 50, 20)
obstacle_ratio = st.sidebar.slider("障碍物比例", 0.0, 0.5, 0.3, 0.05)
heuristic = st.sidebar.selectbox(
    "启发式函数", ["manhattan", "euclidean", "chebyshev", "greedy", "dijkstra"]
)

# 颜色映射
color_map = {
    CellType.EMPTY: "white",
    CellType.OBSTACLE: "black",
    CellType.SEARCHED: "lightblue",
    CellType.PATH: "orange",
    CellType.START: "green",
    CellType.END: "red",
}


# 使用 matplotlib 绘制地图
def plot_map(map_array):
    fig, ax = plt.subplots(figsize=(10, 10))
    cmap = plt.matplotlib.colors.ListedColormap(list(color_map.values()))
    bounds = list(range(len(color_map) + 1))
    norm = plt.matplotlib.colors.BoundaryNorm(bounds, cmap.N)

    ax.imshow(map_array, cmap=cmap, norm=norm)
    ax.grid(which="major", axis="both", linestyle="-", color="k", linewidth=2)
    ax.set_xticks(np.arange(-0.5, len(map_array), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(map_array), 1), minor=True)
    ax.grid(which="minor", axis="both", linestyle="-", color="k", linewidth=1)

    # 隐藏刻度
    ax.set_xticks([])
    ax.set_yticks([])

    # 移除轴标签
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.tight_layout()
    return fig


# 初始化新地图按钮
if st.button("初始化新地图"):
    st.session_state.pathfinder = AStarPathfinder(size, obstacle_ratio, heuristic)
    st.success("新地图已初始化！")

# 显示地图
if st.session_state.pathfinder is not None:
    st.subheader("初始地图")
    st.pyplot(plot_map(st.session_state.pathfinder.get_initial_map()))

    # 运行 A* 算法按钮
    if st.button("运行 A* 算法"):
        result = st.session_state.pathfinder.find_path()

        if result is not None:
            st.subheader("搜索过程和最终路径")
            st.pyplot(plot_map(result))
            st.success("找到路径！")
        else:
            st.error("未找到路径。")
else:
    st.info("请先初始化地图")

# 显示说明
st.sidebar.markdown("""
## 颜色说明
- 白色: 空白区域
- 黑色: 障碍物
- 绿色: 起点
- 红色: 终点
- 蓝色: 已搜索区域
- 橙色: 最终路径
""")
