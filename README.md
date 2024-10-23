# A*寻路算法可视化

这是一个使用Streamlit框架开发的A星寻路算法可视化项目。该项目允许用户交互式地探索A星算法在不同地图配置和启发式函数下的表现。

## 功能特点

- 可视化A*寻路算法的运行过程
- 支持调整地图大小和障碍物比例
- 可切换不同的启发式函数
- 交互式界面，便于实验和学习

## 环境配置

本项目使用Pixi进行环境管理，同时也提供了`requirements.txt`文件以支持传统的Python环境配置。

### 使用Pixi（推荐）

如果您已安装Pixi，可以直接使用项目根目录下的`pixi.lock`文件来复现环境：

```bash
pixi run streamlit run app.py
```

### 使用requirements.txt

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 许可证

本项目采用 MIT 许可证。详情请见 [LICENSE](LICENSE) 文件。
