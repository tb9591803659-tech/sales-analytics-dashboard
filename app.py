from src.data_loader import load_data, save_data
from src.cleaner import clean_data,validate_cleaned_data
from src.analysis import total_sales,total_orders,total_profit,total_quantity,average_order_value,profit_margin,sales_by_category,profit_by_category,profit_by_region,sales_by_region,quantity_by_category,category_summary,regional_summary,yearly_sales,monthly_profit,monthly_sales,top_products_by_sales,top_customers_by_sales,product_performance,top_products_by_profit,correlation_analysis
import os

filepath = input("Enter file name: ")

if not filepath.endswith(".csv"):
    filepath += ".csv"

filepath = os.path.join("data", filepath)

df = load_data(filepath)
1
print(df.columns.tolist())
if df is not None:

    df = clean_data(df)

    output_path = os.path.join("data", "cleaned_data.csv")

    save_data(df, output_path)

    # validate_cleaned_data(df)

    Total_Sales = total_sales(df)
    print("Total  Sales :",Total_Sales)
    print("Total profit :",total_profit(df))
    print("Total Orders :",total_orders(df))
    print("Total Quantity :",total_quantity(df))
    print("Average order Value(AOV) :",average_order_value(df))
    print("Profit Margin: ",profit_margin(df))
    
    # print("\nSales by Category:")
    # print(sales_by_category(df))

    # print("\nSales by Region:")
    # print(sales_by_region(df))

    # print("\nProfit by Category:")
    # print(profit_by_category(df))

    # print("\nProfit by Region:")
    # print(profit_by_region(df))

    # print("\nQuantity by Category:")
    # print(quantity_by_category(df))
    # print("\nCategorical Summary: \n",category_summary(df))
    # print("\nRegional Summary: \n",regional_summary(df)) 
    # print("\nYearly Sales:")
    # print(yearly_sales(df))

    # print("\nMonthly Sales:")
    # print(monthly_sales(df))

    # print("\nMonthly Profit:")
    # print(monthly_profit(df))

    # print("\nTop Products by Sales:")
    # print(top_products_by_sales(df))

    # print("\nTop Products by Profit:")
    # print(top_products_by_profit(df))

    # print("\nTop Customers by Sales:")
    # print(top_customers_by_sales(df))

    # print("\nProduct Performance:")
    # print(product_performance(df).head(10))

    print("\nCorrelation Analysis:")
    print(correlation_analysis(df))

