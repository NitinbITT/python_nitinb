from sqlalchemy import text
from DB_connect import connect_db

query = """
SELECT DISTINCT
    o.salesman_id,
    o.customer_id
FROM inventory_orders o
JOIN inventory_customers c
    ON o.customer_id = c.customer_id
   AND o.salesman_id = c.salesman_id;
"""


def get_salespeople_customers():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))
            rows = result.all()
            if not rows:
                print("No data found.")
                return

            print(f"{'Salesman ID':<15} {'Customer ID':<15}")
            print("-" * 30)

            for row in rows:
                print(f"{row.salesman_id:<15} {row.customer_id:<15}")

    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_salespeople_customers()
