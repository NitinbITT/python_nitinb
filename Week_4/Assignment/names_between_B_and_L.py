'''write a SQL query to retrieve the details of the salespeople whose names begin with any
 letter between 'A' and 'L' (not inclusive). Return salesman_id, name, city, commission.'''

from sqlalchemy import text
from DB_connect import connect_db

query = """
SELECT
    salesman_id,
    name,
    city,
    commission
FROM salesman
WHERE name >= 'B'
  AND name < 'L';
"""


def get_salesmen_in_range():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()

            if not rows:
                print("No data found.")
                return

            print(f"{'Salesman ID':<12} {'Name':<20} {'City':<15} {'Commission':<10}")
            print("-" * 60)
            for row in rows:
                print(
                    f"{row.salesman_id:<12} {row.name:<20} {row.city:<15} {row.commission:<10}"
                )
    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_salesmen_in_range()
