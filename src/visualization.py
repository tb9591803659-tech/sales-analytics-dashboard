import plotly.express as px
import pandas as pd
from src.analysis import sales_by_category,monthly_sales,profit_by_region,top_products_by_sales,correlation_analysis,product_performance

def category_sales_chart(df):
    result = sales_by_category(df).sort_values("Sales",ascending = False)

    fig = px.bar(
    result,
    x="Category",
    y="Sales",
    title="Sales by Category",
    labels={
        "Category": "Category",
        "Sales": "Total Sales"
    }
    )

    return fig

def monthly_sales_chart(df) :
    result = monthly_sales(df)

    result["Date"] = pd.to_datetime(
        result["Year"].astype(str) + '-' 
        + result["Month"].astype(str) + '-01'
    )

    fig = px.line(
        result,
        x = "Date",
        y = "Sales",
        title = "Monthly Sales Trend",
        labels ={
            "Date" : "Date",
            "Sales" : "Total Sales"
        }
        )

    return fig

def profit_by_region_chart(df):
    result = profit_by_region(df)

    result = result.sort_values(
        "Profit",
        ascending=False
    )

    fig = px.bar(
        result,
        x="Region",
        y="Profit",
        title="Profit by Region",
        labels={
            "Region": "Region",
            "Profit": "Total Profit"
        }
    )

    return fig

def top_products_sales_chart(df, n=10):
    result = top_products_by_sales(df, n)

    fig = px.bar(
        result,
        x="Sales",
        y="Product.Name",
        orientation="h",
        title=f"Top {n} Products by Sales",
        labels={
            "Sales": "Total Sales",
            "Product.Name": "Product"
        }
    )
    fig.update_yaxes(autorange = "reversed")
    return fig

def sales_distribution_chart(df):
    fig = px.histogram(
        df,
        x="Sales",
        title="Sales Distribution",
        nbins = 30,
        labels={
            "Sales": "Sales Amount"
        }
    )

    return fig

def sales_vs_profit_chart(df):
    fig = px.scatter(
        df,
        x="Sales",
        y="Profit",
        title="Sales vs Profit",
        color="Category",
        labels={
            "Sales": "Sales",
            "Profit": "Profit"
        }
    )

    return fig

def correlation_heatmap(df) :
    result = correlation_analysis(df)

    fig = px.imshow(
        result,
        text_auto= True,
        title = "Correlation Heatmap"
    )

    return fig

def product_performance_chart(df):
    result = product_performance(df)

    fig = px.scatter(
        result,
        x="Sales",
        y="Profit",
        size="Quantity",
        title="Product Sales vs Profit",
        labels={
            "Sales": "Total Sales",
            "Profit": "Total Profit",
            "Quantity": "Quantity Sold"
        }
    )

    return fig