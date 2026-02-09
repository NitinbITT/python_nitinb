'''Write a SQL query using Aggregate Functions to find the maximum order (purchase) amount for each customer. 
The customer ID should be in the range 3002 and 3007(Begin and end values are included.).
Filter the rows for maximum order (purchase) amount is higher than 1000. Return customer id and maximum purchase amount. 
Add a column named “Shipment Date” with the value being the 7 days after the ord_date. 
Create a column called ins_date(DateTime) and the value of the column is current date-time. 
Creating a column named ‘Data_Latency’ which is a difference of ins_date and shipment_date in days.'''

from sqlalchemy import text
from DB_connect import connect_db

query = """
SELECT
    customer_id,
    MAX(purch_amt) AS max_purchase_amount,
    DATE_ADD(ord_date, INTERVAL 7 DAY) AS shipment_date,
    NOW() AS ins_date,
    DATEDIFF(
        NOW(),
        DATE_ADD(ord_date, INTERVAL 7 DAY)
    ) AS Data_Latency
FROM TableA
WHERE customer_id BETWEEN 3002 AND 3007
GROUP BY customer_id, ord_date
HAVING MAX(purch_amt) > 1000;
"""


def get_max_purchase_info():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()

            if not rows:
                print("No data found.")
                return

            print(
                f"{'Customer ID':<12} {'Max Purchase':<15} {'Shipment Date':<15} {'Insert Date':<20} {'Data Latency':<12}"
            )
            print("-" * 80)
            for row in rows:
                print(
                    f"{row.customer_id:<12} {row.max_purchase_amount:<15} {row.shipment_date:<15} {row.ins_date:<20} {row.Data_Latency:<12}"
                )
    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_max_purchase_info()
