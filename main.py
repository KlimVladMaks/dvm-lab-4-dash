import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})

fig1 = px.line(df, x='x', y='y', title="График 1 (левый столбец)")
fig2 = px.bar(df, x='x', y='y', title="График 2 (левый столбец)")
fig3 = px.scatter(df, x='x', y='y', title="График 3 (правый столбец)")
fig4 = px.pie(df, names='x', values='y', title="График 4 (правый столбец)")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dcc.Graph(figure=fig1),
                        dcc.Graph(figure=fig2),
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(figure=fig3),
                        dcc.Graph(figure=fig4),
                    ],
                    width=6,
                ),
            ]
        )
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run(debug=True)
