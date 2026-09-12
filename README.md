# 📊 Sales Analytics Dashboard

> Interactive business analytics dashboard built with Python, Pandas, Plotly, and Streamlit.

[![Status](https://img.shields.io/badge/Status-Completed%20%26%20Deployed-success?style=for-the-badge)](https://sales-analytics-dashboard-fhl2miiq2o4x6ka3ehvyey.streamlit.app/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://sales-analytics-dashboard-fhl2miiq2o4x6ka3ehvyey.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)

[🚀 Live Demo](https://sales-analytics-dashboard-fhl2miiq2o4x6ka3ehvyey.streamlit.app/) • [📂 GitHub Repository](https://github.com/tb9591803659-tech/sales-analytics-dashboard) • [👤 Author Profile](https://github.com/tb9591803659-tech)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Dashboard Screenshots](#-dashboard-screenshots)
- [Tech Stack](#-tech-stack)
- [Project Architecture](#-project-architecture)
- [Repository Structure](#-repository-structure)
- [File Responsibilities](#-file-responsibilities)
- [Dataset & Validated Business Metrics](#-dataset--validated-business-metrics)
- [Data Cleaning & Validation Pipeline](#-data-cleaning--validation-pipeline)
- [Reproducible Data Preparation](#-reproducible-data-preparation)
- [Local Installation & Setup](#-local-installation--setup)
- [Deployment Details](#-deployment-details)
- [Design Decisions](#-design-decisions)
- [Project Goals](#-project-goals)
- [Learning Outcomes](#-learning-outcomes)
- [Repository Hygiene](#-repository-hygiene)
- [Project Status](#-project-status)
- [Future Improvements](#-future-improvements)
- [Contributing](#-contributing)
- [Issues & Feedback](#-issues--feedback)
- [Author](#-author)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Sales Analytics Dashboard** is an end-to-end data analytics application built using **Python, Pandas, NumPy, Plotly, and Streamlit**. It transforms raw retail transaction data into actionable business intelligence through dynamic KPIs, multi-dimensional filters, trend visualizations, and deep-dive tables.

Rather than running ad-hoc scripts or directly graphing raw CSV files, this project executes a disciplined engineering pipeline:

$$\text{Raw Data} \longrightarrow \text{Cleaning} \longrightarrow \text{Validation} \longrightarrow \text{Analysis} \longrightarrow \text{Visualization} \longrightarrow \text{Interactive Dashboard} \longrightarrow \text{Deployment}$$

The project emphasizes **defensive data validation**, **modular code separation**, **reproducible pipelines**, and **resilient cloud deployment**.

---

## ✨ Key Features

- **Dynamic KPI Overview:** Evaluates core revenue metrics in real time:
  - **Total Sales:** Aggregate revenue formatted in standard currency.
  - **Total Profit:** Overall bottom-line net return.
  - **Total Orders:** Unique transaction count across the enterprise.
  - **Profit Margin:** Percentage margin dynamically updated per filter context.
- **Interactive Multi-Parameter Filters:**
  - Regional segmentation selection.
  - Granular date range picker.
  - Cross-filtering guarantees all visual components, KPIs, and summaries update cohesively.
- **Adaptive Sales Trend Engine:**
  - Displays a **Monthly Sales Trend** when analyzing broad date ranges.
  - Automatically switches to a **Daily Sales Trend** when filtering windows are 31 days or fewer, avoiding aggregated visual flattening.
- **Categorical Revenue Analysis:** Interactive Plotly bar chart mapping volume across product categories.
- **Regional Profitability Breakdown:** Comparative analysis uncovering profit concentrations and regional underperformance.
- **Top Product Rankings:** Horizontal bar chart highlighting the top 10 revenue-generating products.
- **Automated Contextual Insights:** Dynamic summary metrics identifying the highest-selling category, top-performing product, and most profitable region directly within the selected view.
- **Detailed Tabular Exploration:** Interactive data grid displaying transactional granularity (`Order.ID`, `Order.Date`, `Customer.Name`, `Region`, `Category`, `Sub.Category`, `Product.Name`, and `Sales`).

---

## 📸 Dashboard Screenshots

### 1. Dashboard Overview
The primary command center showcasing high-level KPI cards, interactive filters, contextual insights, and adaptive revenue timelines.

![Dashboard Overview](screenshots/dashboard-overview.png)

---

### 2. Sales & Product Analysis
Visual analytics breaking down revenue by category, regional profitability spreads, and the top 10 products by sales volume.

![Sales and Product Analysis](screenshots/dashboard-charts.png)

---

### 3. Detailed Data
Interactive data explorer allowing users to inspect individual transaction records corresponding to active filter conditions.

![Detailed Data](screenshots/dashboard-data.png)

---

## 🛠️ Tech Stack

| Technology | Role & Purpose |
|---|---|
| **Python** | Primary programming language used for end-to-end development |
| **Pandas** | High-performance data structures, transformation, group aggregations, and cleaning |
| **NumPy** | Numerical operations |
| **Plotly** | Declarative, interactive data visualizations with hover cards and dynamic axes |
| **Streamlit** | Interactive UI state handling, reactive component rendering, and caching |
| **Git & GitHub** | Source code management, semantic version control, and collaborative tracking |
| **Streamlit Community Cloud** | Continuous cloud deployment and live application hosting |

---

## 🧠 Project Architecture

```text
                         RAW DATA
                            │
                            ▼
                  ┌──────────────────┐
                  │ data/            │
                  │  superstore.csv  │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │   Data Loading   │
                  │src/data_loader.py│
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │  Data Cleaning   │
                  │  src/cleaner.py  │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │ Data Validation  │
                  │  src/cleaner.py  │
                  └──────────────────┘
                            │
                            ▼
                  cleaned_data.csv
                  (Generated/Ignored)
                            │
                            ▼
                  ┌──────────────────┐
                  │  Data Analysis   │
                  │ src/analysis.py  │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │  Visualization   │
                  │src/visualizat... │
                  └──────────────────┘
                            │
                            ▼
                  ┌──────────────────┐
                  │  Streamlit App   │
                  │     app.py       │
                  └──────────────────┘
                            │
                            ▼
                     LIVE DASHBOARD

📁 Repository Structure
Sales Analytics Dashboard/
│
├── data/
│   └── superstore.csv             # Raw transactional retail dataset
│
├── screenshots/
│   ├── dashboard-charts.png       # Analytical visual section preview
│   ├── dashboard-data.png         # Tabular data explorer preview
│   └── dashboard-overview.png     # Primary KPI and overview preview
│
├── src/
│   ├── __init__.py                # Package initialization marker
│   ├── analysis.py                # Reusable analytical aggregations and metrics
│   ├── cleaner.py                 # Cleaning functions and structural data validation
│   ├── data_loader.py             # CSV ingestion, error handling, and datetime parsing
│   └── visualization.py          # Modular Plotly chart generation routines
│
├── .gitignore                     # Repository hygiene configuration
├── app.py                         # Main Streamlit web application interface
├── prepare_data.py                # Standalone data preparation batch script
├── README.md                      # Comprehensive project documentation
└── requirements.txt               # Application environment dependencies