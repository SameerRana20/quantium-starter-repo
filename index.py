import pandas as pd

data_0 = pd.read_csv("data/daily_sales_data_0.csv")
data_1 = pd.read_csv("data/daily_sales_data_1.csv")
data_2 = pd.read_csv("data/daily_sales_data_2.csv")

data = pd.concat([data_0,data_1,data_2], ignore_index=True)

pink_data= data[data["product"]== "pink morsel"]

pink_data["price"] = pink_data["price"].str.replace("$", "").astype(float)

pink_data["sales"] = pink_data["price"] * pink_data["quantity"]

final_data= pink_data[["sales", "date" , "region"]]
final_data = final_data.rename(columns= {
    "sales": "Sales",
    "date": "Date",
    "region" : "Region"
})

final_data.to_csv("data/formated_sales_data.csv",index=False)

print(final_data)