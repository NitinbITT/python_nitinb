'''Find the names of employees who earn the highest salary in their respective departments. 
Include the department name and salary in the result.  '''

from sqlalchemy import text
from DB_connect import connect_db

query = """
SELECT
    e.employee_name,
    d.department_name,
    s.salary_amount
FROM employees e
JOIN salaries s
    ON e.employee_id = s.employee_id
JOIN departments d
    ON e.department_id = d.department_id
JOIN (
    SELECT
        e.department_id,
        MAX(s.salary_amount) AS max_salary
    FROM employees e
    JOIN salaries s
        ON e.employee_id = s.employee_id
    GROUP BY e.department_id
) ms
    ON e.department_id = ms.department_id
   AND s.salary_amount = ms.max_salary;
"""


def get_highest_salaries():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()

            if not rows:
                print("No data found.")
                return

            print(f"{'Employee Name':<20} {'Department':<15} {'Salary':<10}")
            print("-" * 50)
            for row in rows:
                print(
                    f"{row.employee_name:<20} {row.department_name:<15} {row.salary_amount:<10}"
                )
    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_highest_salaries()
