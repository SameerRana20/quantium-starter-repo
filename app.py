from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/formated_sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

app = Dash(__name__)

app.layout = html.Div([
    
    # Title
    html.H1(
        "Pink Morsel Sales Visualizer",
        style={
            "textAlign": "center",
            "marginBottom": "30px",
            "color": "#333"
        }
    ),

    # Main container
    html.Div([

        # Graph section
        html.Div([
            dcc.Graph(id="sales-graph")
        ],
        style={
            "width": "70%",
            "padding": "20px",
            "backgroundColor": "white",
            "borderRadius": "10px",
            "boxShadow": "0px 0px 10px rgba(0,0,0,0.1)"
        }),

        # Filter section
        html.Div([
            html.H3("Select Region"),

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
            "width": "20%",
            "padding": "20px",
            "backgroundColor": "#f9f9f9",
            "borderRadius": "10px",
            "boxShadow": "0px 0px 10px rgba(0,0,0,0.05)"
        })

    ],
    style={
        "display": "flex",
        "justifyContent": "center",
        "gap": "30px"
    })

],
style={
    "backgroundColor": "#f2f2f2",
    "minHeight": "100vh",
    "padding": "40px"
})


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
