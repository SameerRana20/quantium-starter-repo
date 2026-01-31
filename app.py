from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/formated_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)
 
app.layout = html.Div(
    children=[

    
        html.H1(
            "Pink Morsel Sales Visualizer",
            id="app-header",
            style={
                "textAlign": "center",
                "marginBottom": "30px",
                "color": "#333"
            }
        ),

 
        dcc.Graph(id="sales-graph"),

    
        dcc.RadioItems(
            id="region",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
                {"label": "East", "value": "east"},
            ],
            value="all",
            labelStyle={"display": "block", "margin": "10px 0"}
        )
    ],
    style={
        "backgroundColor": "#f2f2f2",
        "minHeight": "100vh",
        "padding": "40px"
    }
)


@app.callback(
    Output("sales-graph", "figure"),
    Input("region", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"].str.lower() == selected_region]

    daily_sales = filtered_df.groupby("Date")["Sales"].sum().reset_index()
    daily_sales = daily_sales.sort_values(by="Date")

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales",
        labels={"Date": "Date", "Sales": "Total Sales"}
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
