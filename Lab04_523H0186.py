# === Exercise 3: Combined Dashboard (Plotly + Dash) ===
# File: country_population_dashboard_full.py

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go

# === Load and preprocess data ===
df_raw = pd.read_csv("CountryPopulation.csv")

# Reshape wide format → long format
df = df_raw.melt(
    id_vars=["Country Name", "Country Code", "Indicator Name", "Indicator Code"],
    var_name="Year",
    value_name="Population"
)

# Convert year and population to numeric
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["Population"] = pd.to_numeric(df["Population"], errors="coerce")

# Remove missing values
df = df.dropna(subset=["Population"])

# === Create Dash App ===
app = dash.Dash(__name__)
app.title = "World Population Dashboard"

# === Layout ===
app.layout = html.Div([
    html.H1("World Population Dashboard", style={'textAlign': 'center', 'color': '#2E86C1', 'fontSize': 36}),

    html.Div([
        html.Label("Select Country:", style={'fontSize': 22, 'marginRight': '10px'}),
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': c, 'value': c} for c in sorted(df['Country Name'].unique())],
            value='Vietnam',
            style={'width': '400px'}
        )
    ], style={'textAlign': 'center'}),

    html.Br(),

    html.Div([
        html.Label("Select Year:", style={'fontSize': 22, 'marginRight': '10px'}),
        dcc.Slider(
            id='year-slider',
            min=df['Year'].min(),
            max=df['Year'].max(),
            step=1,
            marks={int(y): str(int(y)) for y in range(int(df['Year'].min()), int(df['Year'].max())+1, 5)},
            value=int(df['Year'].max())
        )
    ], style={'width': '80%', 'margin': 'auto'}),

    html.Br(),
    html.Br(),

    html.Div([
        html.Div(dcc.Graph(id='trend-line'), style={'width': '50%'}),
        html.Div(dcc.Graph(id='top10-bar'), style={'width': '50%'})
    ], style={'display': 'flex', 'justify-content': 'center'})
])

# === Callback Function ===
@app.callback(
    [Output('trend-line', 'figure'),
     Output('top10-bar', 'figure')],
    [Input('country-dropdown', 'value'),
     Input('year-slider', 'value')]
)
def update_graphs(selected_country, selected_year):
    # --- Line chart: population trend for selected country ---
    df_country = df[df['Country Name'] == selected_country]
    fig_trend = go.Figure(
        data=go.Scatter(
            x=df_country['Year'],
            y=df_country['Population'],
            mode='lines+markers',
            marker=dict(color='green')
        )
    )
    fig_trend.update_layout(
        title=f"Population Growth of {selected_country} (1960–{int(df['Year'].max())})",
        xaxis_title="Year",
        yaxis_title="Population",
        template='plotly_white'
    )

    # --- Bar chart: top 10 most populous countries in selected year ---
    df_year = df[df['Year'] == selected_year].nlargest(10, 'Population')
    fig_bar = px.bar(
        df_year,
        x='Country Name',
        y='Population',
        color='Country Name',
        title=f"Top 10 Countries by Population in {selected_year}",
    )
    fig_bar.update_layout(xaxis_title="Country", yaxis_title="Population")

    return fig_trend, fig_bar


# === Run the app ===
if __name__ == '__main__':
    app.run(debug=True)