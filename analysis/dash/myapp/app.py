import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.DataFrame({'x': range(50), 'y': range(50)})

app.layout = html.Div([
    dcc.Graph(figure=px.scatter(df, x='x', y='y')),
])
if __name__ == '__main__':
    app.run(debug=True)

