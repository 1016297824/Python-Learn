# pyecharts入门
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts

# 基础折线图
line = Line()

# 给折线图添加X轴数据
line.add_xaxis(["霸气可爱小蜜蜂", "霸气可爱小州官", "霸气可爱小懒虫"])
# 给折线图添加Y轴数据
line.add_yaxis("体重（单位：斤）", [120, 130, 140])

# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title="体检", pos_left="center", pos_bottom="0"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True, min_=100, max_=160),
)

# 生成图像
line.render()
