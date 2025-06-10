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
"""
- Указать число стран для каждой части света.
"""
df = pd.read_csv('dataset_2.csv')

fig2 = px.bar(
    df,
    x='Часть света',
    y='Медиана',
    title='Медианное значение уровня удовлетворённости жизнью по частям света (2024)',
    labels={'Медиана': 'Медиана', 'Часть света': 'Часть света'},
    color='Часть света',
    text='Медиана'
)

fig2.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig2.update_layout(
    showlegend=False,
    height=550,
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    yaxis_title='Медиана',
    xaxis_title='',
    title_x=0.5
)

# ---------- Диаграмма 3 ----------

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        top10_table
                    ],
                    width=6,
                ),
                dbc.Col(
                    [
                        dcc.Graph(figure=fig2)
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
