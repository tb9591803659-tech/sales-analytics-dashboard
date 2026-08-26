import pandas as pd 

def total_sales(df):
    return round(df["Sales"].sum(),2)

def total_profit(df):
    return round(df["Profit"].sum(),2)

def total_orders(df) :
    return df["Order.ID"].nunique()

def total_quantity(df):
    return df["Quantity"].sum()

def average_order_value(df):
    total_sales = df["Sales"].sum()
    total_orders = df["Order.ID"].nunique()

    return round(total_sales / total_orders,2)

def profit_margin(df) :
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    if total_sales == 0 :
        return 0
    return round((float)(total_profit/total_sales)*100,2)

def sales_by_category(df):
    return df.groupby("Category")["Sales"].sum().reset_index()

def sales_by_region(df):
    return df.groupby("Region")["Sales"].sum().reset_index()

def profit_by_category(df):
    return df.groupby("Category")["Profit"].sum().reset_index()

def profit_by_region(df):
    return df.groupby("Region")["Profit"].sum().reset_index()

def quantity_by_category(df):
    return df.groupby("Category")["Quantity"].sum().reset_index()

def category_summary(df):
    return df.groupby("Category").agg({
    "Sales": ["sum", "mean", "max", "min"],
    "Profit": ["sum", "mean"],
    "Quantity": "sum"
})

def regional_summary(df):
    return df.groupby("Region").agg({
        "Sales": ["sum", "mean", "max", "min"],
        "Profit": "sum",
        "Quantity": "sum"
    }).reset_index()

def yearly_sales(df):
    analysis_df = df.copy()

    analysis_df["Year"] = analysis_df["Order.Date"].dt.year

    return (
        analysis_df
        .groupby("Year")["Sales"]
        .sum()
        .reset_index()
    )

def monthly_sales(df):
    analysis_df = df.copy()

    analysis_df["Year"] = analysis_df["Order.Date"].dt.year
    analysis_df["Month"] = analysis_df["Order.Date"].dt.month

    return (
        analysis_df
        .groupby(["Year", "Month"])["Sales"]
        .sum()
        .reset_index()
    )

def monthly_profit(df):
    analysis_df = df.copy()

    analysis_df["Year"] = analysis_df["Order.Date"].dt.year
    analysis_df["Month"] = analysis_df["Order.Date"].dt.month

    return (
        analysis_df
        .groupby(["Year", "Month"])["Profit"]
        .sum()
        .reset_index()
    )

def top_products_by_sales(df, n=10):
    result = (
        df.groupby("Product.Name")["Sales"]
        .sum()
        .reset_index()
    )

    return result.sort_values(
        "Sales",
        ascending=False
    ).head(n)

def top_products_by_profit(df, n=10):
    result = (
        df.groupby("Product.Name")["Profit"]
        .sum()
        .reset_index()
    )

    return result.sort_values(
        "Profit",
        ascending=False
    ).head(n)

def top_customers_by_sales(df, n=10):
    result = (
        df.groupby(["Customer.ID", "Customer.Name"])["Sales"]
        .sum()
        .reset_index()
    )

    return result.sort_values(
        "Sales",
        ascending=False
    ).head(n)

def product_performance(df):
    result = (
        df.groupby("Product.Name")
        .agg({
            "Sales": "sum",
            "Profit": "sum",
            "Quantity": "sum"
        })
        .reset_index()
    )

    result["Profit Margin"] = (
    result["Profit"]
    .div(result["Sales"].replace(0, pd.NA))
    .mul(100)
    )
    return result

def correlation_analysis(df):
    columns = [
        "Sales",
        "Profit",
        "Quantity",
        "Discount"
    ]

    return df[columns].corr()