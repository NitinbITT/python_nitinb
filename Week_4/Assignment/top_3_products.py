from sqlalchemy import text
from DB_connect import connect_db

query = """
WITH ProductSales AS (
    SELECT
        s.ProductID,
        SUM(s.Quantity) AS total_units_sold,
        SUM(s.Quantity * p.Price) AS total_sales_amount,
        MAX(s.SaleDate) AS last_sale_date
    FROM warehouse_sales_table s
    JOIN warehouse_product_table p 
        ON s.ProductID = p.ProductID
    GROUP BY s.ProductID
),
RecentCustomer AS (
    SELECT
        ps.ProductID,
        c.CustomerName,
        c.Email
    FROM ProductSales ps
    JOIN warehouse_sales_table s
        ON ps.ProductID = s.ProductID
       AND s.SaleDate = ps.last_sale_date
    JOIN warehouse_customers_table c
        ON s.CustomerID = c.CustomerID
)
SELECT
    p.ProductName,
    p.Category,
    ps.total_sales_amount,
    ps.total_units_sold,
    rc.CustomerName,
    rc.Email
FROM ProductSales ps
JOIN warehouse_product_table p 
    ON ps.ProductID = p.ProductID
JOIN RecentCustomer rc 
    ON ps.ProductID = rc.ProductID
ORDER BY ps.total_sales_amount DESC, ps.total_units_sold DESC
LIMIT 3;
"""


def get_top_products():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))
            rows = result.all()
            if not rows:
                print("No data found.")
                return

            print(
                f"{'Product Name':<20} {'Category':<15} {'Total Sales':<15} {'Units Sold':<12} {'Customer Name':<20} {'Email':<25}"
            )
            print("-" * 110)

            for row in rows:
                print(
                    f"{row.ProductName:<20} "
                    f"{row.Category:<15} "
                    f"{row.total_sales_amount:<15} "
                    f"{row.total_units_sold:<12} "
                    f"{row.CustomerName:<20} "
                    f"{row.Email:<25}"
                )

    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_top_products()
