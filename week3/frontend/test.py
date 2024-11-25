import altair as alt
import pandas as pd

# 创建一个示例汽车数据集
data = {
    'Horsepower': [130, 165, 150, 140, 198, 95, 105, 120, 160, 110],
    'Miles_per_Gallon': [18, 15, 18, 16, 15, 24, 22, 20, 17, 19],
    'Origin': ['USA', 'USA', 'USA', 'USA', 'USA', 'Europe', 'Europe', 'Japan', 'Japan', 'Japan']
}

# 将数据转换为 DataFrame
cars = pd.DataFrame(data)

# 将数据转换为 DataFrame
cars = pd.DataFrame(data)

# 获取用户输入的马力范围
# min_hp = float(input("请输入最小马力："))
# max_hp = float(input("请输入最大马力："))
min_hp = float(input("请输入最小马力："))
max_hp = float(input("请输入最大马力："))
# 根据用户输入的马力范围过滤数据
filtered_cars = cars[(cars['Horsepower'] >= min_hp) & (cars['Horsepower'] <= max_hp)]


chart = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin'
)
chart.display()