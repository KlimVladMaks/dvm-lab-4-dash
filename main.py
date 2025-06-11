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
df = pd.read_csv('dataset_2.csv')

fig2 = px.bar(
    df,
    x='Часть света',
    y='Медиана',
    title='Медианное значение уровня удовлетворённости жизнью<br>по частям света (2024)',
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
df = pd.read_csv('dataset_3.csv')

fig3 = px.line(
    df,
    x='Год',
    y=['Медиана', 'Топ-10 худших', 'Топ-10 лучших'],
    title='Динамика мирового медианного уровня удовлетворённости жизнью',
    labels={'value': 'Уровень удовлетворённости', 'variable': 'Показатель'},
    color_discrete_map={
        'Медиана': 'blue',
        'Топ-10 худших': 'red',
        'Топ-10 лучших': 'green'
    }
)

# ---------- Диаграмма 4 ----------
df_population = pd.read_csv('dataset_4.csv')
population_by_category = df_population.groupby('Категория')['Население'].sum().reset_index()

fig4 = px.pie(
    population_by_category,
    values='Население',
    names='Категория',
    title='Число людей, проживающих в странах с уровнем<br>удовлетворённости жизнью выше/ниже медианного (2024)',
    color='Категория',
    color_discrete_map={
        'Выше медианы': 'green',
        'Ниже медианы': 'red'
    }
)

fig4.update_traces(
    textinfo='percent+label',
    hovertemplate='<b>%{label}</b><br>Население: %{value:,}'
)
fig4.update_layout(
    showlegend=False
)

# ---------- Диаграмма 5 ----------
df_growth = pd.read_csv('dataset_5.csv').head(10)
df_growth = df_growth.sort_values('Динамика', ascending=True)

fig5 = px.bar(
    df_growth,
    x='Динамика',
    y='Название',
    orientation='h',
    title='Топ-10 стран с самым высоким ростом уровня удовлетворенности жизнью<br>с 2011 по 2024 годы',
    color_discrete_sequence=['#1E90FF'],
    text='Динамика'
)

fig5.update_layout(
    showlegend=False
)

# ---------- Диаграмма 6 ----------
df_decline = pd.read_csv('dataset_5.csv').tail(10).sort_values('Динамика', ascending=False)

fig6 = px.bar(
    df_decline,
    x='Динамика',
    y='Название',
    orientation='h',
    title='Топ-10 стран с самым большим падением уровня удовлетворённости<br>жизнью с 2011 по 2024 годы',
    color_discrete_sequence=['#FF6347'],  # Красивый красный цвет (Tomato)
    text='Динамика'
)

fig6.update_layout(
    showlegend=False
)

# ---------- Диаграмма 7 ----------
df_categories = pd.read_csv('dataset_6.csv')

category_counts = df_categories['Категория'].value_counts().reset_index()
category_counts.columns = ['Категория', 'Количество стран']

color_map = {
    'Рост >10%': '#00FF00',
    'Рост 0-10%': "#67FA67",
    'Падение 0-10%': "#FF5F5F",
    'Падение >10%': '#FF0000'
}

fig7 = px.pie(
    category_counts,
    values='Количество стран',
    names='Категория',
    title='Разбивка стран по уровню роста/падения уровня удовлетворённости<br>жизнью с 2011 по 2024 годы',
    color='Категория',
    color_discrete_map=color_map,
    category_orders={
        "Категория": ['Рост >10%', 'Рост 0-10%', 'Падение 0-10%', 'Падение >10%']
    }
)

fig7.update_traces(
    textinfo='label+value',
    textposition='inside',
    hovertemplate='<b>%{label}</b><br>Количество стран: %{value}<br>Доля: %{percent}',
    marker=dict(line=dict(color='#FFFFFF', width=1))
)

fig7.update_layout(
    uniformtext_minsize=12,
    uniformtext_mode='hide',
    showlegend=False,
    margin=dict(t=80, b=30, l=30, r=30)
)

# ---------- Дашборд -----------
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1("Уровень удовлетворённости жизнью в мире", 
                        className="text-center mt-2 mb-2"),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.H2("(Уровень удовлетворённости жизнью оценивается по шкале от 0 до 10)",
                        className="text-center mb-4 text-muted"),
                width=12
            )
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(top10_table, className="border border-dark"),
                        dcc.Graph(figure=fig3, className="border border-dark"),
                        dcc.Graph(figure=fig5, className="border border-dark"),
                        dcc.Graph(figure=fig7, className="border border-dark")
                    ],
                    width=6,
                    className="pe-0"
                ),
                dbc.Col(
                    [
                        dcc.Graph(figure=fig2, className="border border-dark"),
                        dcc.Graph(figure=fig4, className="border border-dark"),
                        dcc.Graph(figure=fig6, className="border border-dark")
                    ],
                    width=6,
                    className="ps-0"
                ),
            ]
        )
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run(debug=True)
