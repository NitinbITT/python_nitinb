from sqlalchemy import text
from DB_connect import connect_db

query = """
SELECT 
    h.hacker_id,
    h.name,
    SUM(s.max_score) AS total_score
FROM hackers h
JOIN (
    SELECT hacker_id, MAX(score) AS max_score
    FROM submissions
    GROUP BY hacker_id, challenge_id
) s
ON h.hacker_id = s.hacker_id
GROUP BY h.hacker_id, h.name
HAVING total_score > 0
ORDER BY total_score DESC, h.hacker_id;
"""


def get_top_hackers():
    try:
        engine = connect_db()
        with engine.begin() as conn:
            result = conn.execute(text(query))
            rows = result.fetchall()

            if not rows:
                print("No data found.")
                return

            print(f"{'Hacker ID':<10} {'Name':<20} {'Total Score':<12}")
            print("-" * 45)
            for row in rows:
                print(f"{row.hacker_id:<10} {row.name:<20} {row.total_score:<12}")
    except Exception as e:
        print("Error executing query:", e)


if __name__ == "__main__":
    get_top_hackers()
