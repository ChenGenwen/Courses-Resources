import pyecharts.options as opts
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from pyecharts.charts import Line


x = ['第一天', '第六天', '第十一天', '第十六天', '第二十一天', '第二十六天', '第三十天']
y1 = [269, 258, 263, 262, 274, 278, 293]
y2 = [270, 279, 279, 258, 257, 272, 290]
y3 = [272, 274, 271, 261, 269, 274, 270]
y4 = [274, 279, 270, 269, 287, 259, 266]
y5 = [270, 269, 287, 278, 270, 272, 280]
y6 = [270, 263, 259, 276, 288, 278, 280]
y7 = [274, 274, 278, 272, 267, 276, 268]
y8 = [276, 298, 290, 283, 277, 283, 270]

line = (
    Line()
        .add_xaxis(xaxis_data=x)
        .add_yaxis(series_name="体育馆", y_axis=y1, symbol="arrow", is_symbol_show=False)
        .add_yaxis(series_name="综合楼", y_axis=y2)
        .add_yaxis(series_name="教学区", y_axis=y3,symbol="circle")
        .add_yaxis(series_name="图书馆", y_axis=y4,symbol="rect")
        .add_yaxis(series_name="信息楼", y_axis=y5,symbol="roundRect")
        .add_yaxis(series_name="篮球场", y_axis=y6,symbol="triangle")
        .add_yaxis(series_name="宿舍", y_axis=y7,symbol="pin")
        .add_yaxis(series_name="食堂", y_axis=y8,symbol="diamond")
        .set_global_opts(title_opts=opts.TitleOpts(title="温度变化折线图"))
)

line.render()
