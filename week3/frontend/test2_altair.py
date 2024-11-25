import altair as alt
import pandas as pd

# 创建示例数据
data = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 30, 40]
})

# 创建图表
chart = alt.Chart(data).mark_point().encode(
    x='x',
    y='y'
)

# 显示图表
chart.show()
chart.save('chart.html')