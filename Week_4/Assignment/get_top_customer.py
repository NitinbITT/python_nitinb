from sqlalchemy import text
from DB_connect import connect_db

query = """
SELECT 
    customer_id, 
    COUNT(order_id) AS total_order, 
    GROUP_CONCAT(order_date SEPARATOR ',') AS order_dates
FROM orders
GROUP BY customer_id
ORDER BY total_order DESC, customer_id ASC
LIMIT 1;
"""


def get_top_customer():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))
            row = result.fetchone()
            if row:
                print(f"Customer ID: {row.customer_id}")
                print(f"Total Orders: {row.total_order}")
                print(f"Order Dates: {row.order_dates}")
            else:
                print("No data found.")
    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_top_customer()
