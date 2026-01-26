from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("data/formated_sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"])

daily_sales = df.groupby("Date")["Sales"].sum().reset_index()

daily_sales = daily_sales.sort_values(by="Date")

chart = px.line(
    daily_sales, 
    x = "Date",
    y = "Sales",
    title= "Pink Morsel Sales",
labels={"Date": "Date", "Sales": "Total Sales"}

)

app =Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualizer"),
    html.Div([
        dcc.Graph(id="sales-graph"),
        dcc.RadioItems(
            options=[
            {"label":"All", "value":"all"},
            {"label":"North", "value":"north"},
            {"label":"South", "value":"south"},
            {"label":"West", "value":"west"},
            {"label":"East", "value":"east"},
        ], value="all")
        ],
     style= {"display": "flex" , "align-items": "center", "justifyContent": "center","gap": "40px" })
 
])

@callback(
    Output( "sales-graph" ,"chart"),
    Input("region"))
)

if __name__ == "__main__": 
    app.run(debug=True)