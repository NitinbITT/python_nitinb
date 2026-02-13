''' Julia needs your expertise again for another coding contest challenge! 
This time, the task is to calculate the total score of each hacker, which is the sum of their maximum scores for all challenges. 
Write a query to print the hacker_id, name, and total score of the hackers. Order the results by the descending total score.
If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. 
Exclude all hackers with a total score of 0 from your result.  '''

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
