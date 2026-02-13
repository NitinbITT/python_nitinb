from sqlalchemy import create_engine,text
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()
try:
    password=quote_plus(os.getenv("PASSWORD"))
    engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/practice")
    print("Connected DB")
    with engine.connect() as connection:
        result =connection.execute(text("Select * from student"))
        print(result)
        for row in result:
            print(row)
except Exception as e:
    print(e,"Error in connecting DB")

# from sqlalchemy import create_engine,text
# try:
#     engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
#     with engine.connect() as conn:
#         t=text("Show tables")
#         result=conn.execute(t)
#         print(result)
#     print("Connected DB")
# except Exception as e:
#     print(e,"Error connecting to DB")
# import mysql.connector

# try:
#     print("Started")
#     connection=mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password=os.getenv("PASSWORD"),
#         database="practice"
#     )
#     if connection.is_connected():
#         print("Connected to database")
#         cursor = connection.cursor()
#         query="Select * from student"
#         cursor.execute(query)
#         results = cursor.fetchall()
#         for row in results:
#             print(row)



# except Exception as e:
#     print(e,"Erroe connecting to db")