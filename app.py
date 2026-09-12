
import os

from src.data_loader import load_data
from src.cleaner import clean_data, validate_cleaned_data

from src.analysis import (
    total_sales,
    total_orders,
    total_profit,
    profit_margin,
    sales_by_category,
    profit_by_region
)

from src.visualization import (
    monthly_sales_chart,
    category_sales_chart,
    profit_by_region_chart,
    top_products_sales_chart
)

import os
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_dashboard_data(filepath):
    return load_data(filepath)
    

st.title("Interactive Sales Analytics Dashboard")

st.caption(
    "Explore sales performance across regions, categories, products, and time."
)


RAW_DATA_PATH = "data/superstore.csv"
CLEANED_DATA_PATH = "data/cleaned_data.csv"


if not os.path.exists(CLEANED_DATA_PATH):

    raw_df = load_data(RAW_DATA_PATH)

    if raw_df is None:
        st.error("Failed to load the raw dataset.")
        st.stop()

    cleaned_df = clean_data(raw_df)

    if not validate_cleaned_data(cleaned_df):
        st.error("Data validation failed.")
        st.stop()

    cleaned_df.to_csv(
        CLEANED_DATA_PATH,
        index=False
    )


df = load_dashboard_data(CLEANED_DATA_PATH)


    
if df is not None:

    st.sidebar.title("Dashboard Filters")

    st.sidebar.caption(
        "Use the controls below to explore the data."
    )

    st.subheader("Performance Overview")

    regions = ["All"] + sorted(df["Region"].dropna().unique().tolist())

    region = st.sidebar.selectbox(
    "Select Region",
    regions
    )

    categories = ["All"] + sorted(df["Category"].dropna().unique().tolist())

    category = st.sidebar.selectbox(
        "Select Category",
        categories
    )

    filtered_df = df.copy()

    if region != "All":
        filtered_df = filtered_df[filtered_df["Region"] == region]

    if category != "All":
        filtered_df = filtered_df[filtered_df["Category"] == category]

    min_date = df["Order.Date"].min().date()
    max_date = df["Order.Date"].max().date()

    date_range = st.sidebar.date_input(
            "Select Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )

    st.sidebar.divider()

    st.sidebar.caption("Active Filters")

    st.sidebar.write(f"Region: {region}")
    st.sidebar.write(f"Category: {category}")

    if len(date_range) == 2:
        start_date, end_date = date_range

        start_datetime = pd.to_datetime(start_date)
        end_datetime = pd.to_datetime(end_date) + pd.Timedelta(days=1)

        filtered_df = filtered_df[
            (filtered_df["Order.Date"] >= start_datetime)
            &
            (filtered_df["Order.Date"] < end_datetime)
        ]

    if filtered_df.empty:

        st.warning(
            "No data is available for the selected filters. "
            "Try changing the region, category, or date range."
        )

        st.stop()

    
    # Dashboard content
    st.caption(
    f"Showing {len(filtered_df)} records based on the selected filters."
)

    sales = total_sales(filtered_df)
    profit = total_profit(filtered_df)
    orders = total_orders(filtered_df)
    margin = profit_margin(filtered_df)

    col1,col2,col3,col4 = st.columns(4)
    
    #KPIs
    col1.metric(
        "Total Sales",
        f"${sales:,.2f}"
    )

    col2.metric(
        "Total Profit",
        f"${profit:,.2f}"
    )

    col3.metric(
        "Total Orders",
        f"{orders:,}"
    )

    col4.metric(
        "Profit Margin",
        f"{margin:.2f}%"
    )

    category_data = sales_by_category(filtered_df)

    best_category = category_data.loc[
        category_data["Sales"].idxmax(),
        "Category"
    ]


    region_data = profit_by_region(filtered_df)

    best_region = region_data.loc[
        region_data["Profit"].idxmax(),
        "Region"
    ]

    
    #Data insights
    st.subheader("Key Insights")

    st.write(
        f"🏆 Highest selling category: **{best_category}**"
    )

    st.write(
        f"📈 Most profitable region: **{best_region}**"
    )

    st.subheader("Sales Trend Over Time")


    #Visualizations
    fig = monthly_sales_chart(filtered_df)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Sales by Category")

        fig = category_sales_chart(filtered_df)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with col2:
        st.subheader("Profit by Region")

        fig = profit_by_region_chart(filtered_df)

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    st.subheader("Top Products by Sales")

    fig = top_products_sales_chart(
        filtered_df,
        n=10
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
    
    #Filtered Data
    st.divider()

    st.subheader("Detailed Data")

    display_columns = [
        "Order.ID",
        "Order.Date",
        "Customer.Name",
        "Region",
        "Category",
        "Sub.Category",
        "Product.Name",
        "Sales"
    ]

    st.caption(
        "Explore the records matching your selected filters."
    )

    st.dataframe(
        filtered_df[display_columns],
        use_container_width=True,
        hide_index=True
    )

else:
        st.error("Failed to load data.")
        st.stop()
        

        

        