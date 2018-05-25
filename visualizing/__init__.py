import pandas
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff

df = pandas.read_csv('../data.csv')

table = ff.create_table(df)

plotly.offline.plot(table, filename='visuals/chart.html')

trace = go.Scatter(x=df['time'], y=df['value'])
layout = go.Layout(title='data from csv', plot_bgcolor='rgb(200, 200, 200)')
figure = go.Figure(data=[trace], layout=layout)
plotly.offline.plot(figure, filename='visuals/graph.html')
