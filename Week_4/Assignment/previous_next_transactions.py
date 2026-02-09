from sqlalchemy import text
from DB_connect import connect_db

query = """
SELECT
    transaction_date,
    product_name,
    revenue,
    LAG(revenue) OVER (ORDER BY transaction_date) AS prev_revenue,
    LEAD(revenue) OVER (ORDER BY transaction_date) AS next_revenue
FROM transaction_table
ORDER BY transaction_date;
"""


def get_transaction_revenue_with_lag_lead():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))
            rows = result.all()
            if not rows:
                print("No data found.")
                return

            print(
                f"{'Transaction Date':<15} {'Product Name':<15} {'Revenue':<10} {'Prev Revenue':<15} {'Next Revenue':<15}"
            )
            print("-" * 70)

            for row in rows:
                prev_rev = row.prev_revenue if row.prev_revenue is not None else "NULL"
                next_rev = row.next_revenue if row.next_revenue is not None else "NULL"

                print(
                    f"{row.transaction_date:<15} "
                    f"{row.product_name:<15} "
                    f"{row.revenue:<10} "
                    f"{prev_rev:<15} "
                    f"{next_rev:<15}"
                )

    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_transaction_revenue_with_lag_lead()
