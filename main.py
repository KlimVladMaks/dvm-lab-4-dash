import dash
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# ---------- Диаграмма 1 ----------
df = pd.read_csv('dataset_1.csv')
top10_df = df.sort_values(by='Уровень удовлетворённости жизнью', ascending=False).head(10)

top10_table = dbc.Card(
    [
        dbc.CardHeader(html.H6("Топ-10 стран по уровню удовлетворённости жизнью в 2024 году", 
                              className="text-center",
                              style={'margin-top': '5px'}
                              )),
        dbc.CardBody(
            dash_table.DataTable(
                id='top10-table',
                columns=[{"name": i, "id": i} for i in top10_df.columns],
                data=top10_df.to_dict('records'),
                style_table={'overflowX': 'auto'},
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                },
                style_cell={
                    'textAlign': 'left',
                    'padding': '5px'
                },
                page_size=10
            )
        )
    ],
    className="mb-4"
)

# ---------- Диаграмма 2 ----------

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 20, 30, 40, 50]
})

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
                        top10_table,
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
