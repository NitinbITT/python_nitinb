"""Assume you have a table named Orders with columns OrderID (primary key), CustomerID (foreign key), OrderDate, and TotalAmount.
 Write an SQL script that inserts a new order into the Orders table.
However, implement a TRY-CATCH block to handle potential exceptions.

If the specified CustomerID does not exist in the Customers table, raise a custom exception stating "Invalid CustomerID. Please provide a valid CustomerID."

If there is an issue with the insertion (e.g., a violation of a unique constraint or a data type mismatch), catch the exception and print a user-friendly error message.
Create a column named ‘Full Name’ which is the concatenation of first_name and last_name.
Select all the customers with last_name being Doe"""

from sqlalchemy import text
from DB_connect import connect_db

order_id_to_insert = 5
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
insert_order_query = """
INSERT INTO orders_a
VALUES (:oid, :cid, :odate, :amt);
"""


class InvalidCustomerIDException(Exception):
    def __init__(self, message):
        super().__init__(message)

    pass


def insert_order_and_get_customers():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            try:
                conn.execute(
                    text(insert_order_query),
                    {
                        "oid": order_id_to_insert,
                        "cid": customer_id_to_insert,
                        "odate": order_date_to_insert,
                        "amt": total_amount_to_insert,
                    },
                )
                print(f"Order inserted successfully for CustomerID.")

            except Exception as e:
                print(f"Error inserting order: {e}")

            result = conn.execute(
                text("SELECT * FROM customers_a WHERE customer_id = :cid"), {"cid": 1}
            ).fetchone()

            if not result:
                raise InvalidCustomerIDException(
                    "Invalid CustomerID. Please provide a valid CustomerID."
                )
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
