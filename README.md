# 📊 Sales Analytics Dashboard

An interactive sales analytics dashboard built with **Python, Pandas, NumPy, Plotly, and Streamlit** to explore sales performance, profitability, products, categories, regions, and business trends through an interactive web interface.

The project follows a modular and reproducible data pipeline:

**Raw Data → Cleaning → Validation → Analysis → Visualization → Interactive Dashboard → Deployment**

---

## 🚀 Live Demo

🔗 **Live Dashboard:**  
YOUR-STREAMLIT-APP-URL

🔗 **GitHub Repository:**  
YOUR-GITHUB-REPO-URL

> The dashboard is deployed using Streamlit Community Cloud.

---

## 📌 Project Overview

This project transforms a raw Superstore sales dataset into an interactive business analytics dashboard.

The dashboard allows users to:

- Explore sales performance
- Analyze profitability
- Compare regional performance
- Compare product categories
- Identify top-performing products
- Analyze sales trends over time
- Filter data interactively
- Inspect the underlying filtered records

The project was designed with a focus on **clean data processing, modular Python code, reusable analysis functions, interactive visualization, and reproducible deployment**.

---

# ✨ Features

## 📈 KPI Overview

The dashboard provides four key performance indicators:

- **Total Sales**
- **Total Profit**
- **Total Orders**
- **Profit Margin**

The KPIs dynamically update according to the selected filters.

---

## 🎛️ Interactive Filters

Users can interactively filter the dashboard using:

- Region
- Date range

All major dashboard components update based on the selected filters.

---

## 📅 Sales Trend Analysis

The dashboard automatically adapts the sales trend visualization according to the selected date range.

### Longer date ranges

Displays:

**Monthly Sales Trend**

### Short date ranges

Displays:

**Daily Sales Trend**

This makes the visualization more useful when users zoom into a smaller period.

---

## 🏷️ Sales by Category

Visualizes total sales across product categories.

This helps identify which categories contribute the most to overall revenue.

---

## 🌎 Profit by Region

Compares total profit across different regions.

This provides a quick view of regional profitability and helps identify stronger and weaker-performing regions.

---

## 🏆 Top Products

Displays the **Top 10 Products by Sales**.

Products are ranked based on their total sales contribution.

---

## 💡 Key Insights

The dashboard provides automatically generated insights based on the currently filtered dataset.

Examples include:

- Highest-performing category
- Most profitable region
- Top-selling product
- Overall sales performance

---

## 📋 Detailed Data

A detailed data table allows users to inspect the records corresponding to their selected filters.

Displayed information includes:

- Order ID
- Order Date
- Customer
- Region
- Category
- Sub-Category
- Product
- Sales

---

# 📸 Dashboard Screenshots

## 1. Dashboard Overview

The main dashboard provides interactive filters, KPI metrics, key insights, and sales performance over time.

![Dashboard Overview](screenshots/dashboard-overview.png)

---

## 2. Sales & Product Analysis

This section provides sales-by-category analysis, regional profitability, and the top 10 products by sales.

![Sales and Product Analysis](screenshots/dashboard-charts.png)

---

## 3. Detailed Data

The detailed data section allows users to explore the records matching their selected filters.

![Detailed Data](screenshots/dashboard-data.png)

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading, cleaning, transformation, and analysis |
| NumPy | Numerical operations |
| Plotly | Interactive visualizations |
| Streamlit | Dashboard and web application |
| Git | Version control |
| GitHub | Source code and project hosting |
| Streamlit Community Cloud | Deployment |

---

# 🧠 Project Architecture

```text
                         RAW DATA
                            │
                            ▼
                  ┌──────────────────┐
                  │ superstore.csv   │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │  Data Loading    │
                  │ data_loader.py   │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ Data Cleaning    │
                  │   cleaner.py     │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ Data Validation   │
                  │   cleaner.py     │
                  └──────────────────┘
                            │
                            ▼
                  cleaned_data.csv
                            │
                            ▼
                  ┌──────────────────┐
                  │ Data Analysis    │
                  │   analysis.py    │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ Visualization    │
                  │ visualization.py │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ Streamlit App    │
                  │     app.py       │
                  └──────────────────┘
                            │
                            ▼
                     LIVE DASHBOARD