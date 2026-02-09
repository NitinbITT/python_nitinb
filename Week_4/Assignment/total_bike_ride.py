from sqlalchemy import text
from DB_connect import connect_db

query = """
SELECT
    ride_id,
    start_terminal,
    end_terminal,
    ride_duration,
    ROW_NUMBER() OVER (
        PARTITION BY end_terminal
        ORDER BY ride_duration DESC
    ) AS row_num,
    SUM(ride_duration) OVER (
        PARTITION BY end_terminal
        ORDER BY ride_duration DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_duration
FROM ride_table;
"""


def get_bike_rides_running_total():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))

            rows = result.all()
            if not rows:
                print("No data found.")
                return

            print(
                f"{'Ride ID':<8} {'Start Terminal':<20} {'End Terminal':<20} {'Duration':<10} {'Row #':<6} {'Running Total':<15}"
            )
            print("-" * 90)

            for row in rows:
                print(
                    f"{row.ride_id:<8} "
                    f"{row.start_terminal:<20} "
                    f"{row.end_terminal:<20} "
                    f"{row.ride_duration:<10} "
                    f"{row.row_num:<6} "
                    f"{row.running_total_duration:<15}"
                )

    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_bike_rides_running_total()
