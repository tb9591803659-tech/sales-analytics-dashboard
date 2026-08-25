
def total_sales(df):
    return df["Sales"].sum()

def total_profit(df):
    return df["Profit"].sum()

def total_orders(df) :
    return df["Order ID"].nunique()

def total_quantity(df):
    return df["Quantity"].sum()