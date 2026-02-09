from sqlalchemy import text
from DB_connect import connect_db

customer_id_to_insert = 1
order_date_to_insert = "2023-03-15"
total_amount_to_insert = 75.50

select_doe_customers_query = """
SELECT 
    customer_id,
    CONCAT(first_name, ' ', last_name) AS `Full Name`,
    first_name,
    last_name,
    age
FROM customers_a
WHERE last_name = 'Doe';
"""


def insert_order_and_get_customers():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            try:
                conn.execute(
                    text("CALL InsertOrder(:cid, :odate, :amt)"),
                    {
                        "cid": customer_id_to_insert,
                        "odate": order_date_to_insert,
                        "amt": total_amount_to_insert,
                    },
                )
                print(
                    f"Order inserted successfully for CustomerID {customer_id_to_insert}."
                )
            except Exception as e:
                print(f"Error inserting order: {e}")

            result = conn.execute(text(select_doe_customers_query))
            rows = result.mappings().all()

            if not rows:
                print("No customers with last name 'Doe' found.")
                return

            print(
                f"\n{'Customer ID':<12} {'Full Name':<25} {'First Name':<15} {'Last Name':<15} {'Age':<5}"
            )
            print("-" * 80)

            for row in rows:
                print(
                    f"{row['customer_id']:<12} "
                    f"{row['Full Name']:<25} "
                    f"{row['first_name']:<15} "
                    f"{row['last_name']:<15} "
                    f"{row['age']:<5}"
                )

    except Exception as e:
        print("Database connection/query error:", e)


if __name__ == "__main__":
    insert_order_and_get_customers()
