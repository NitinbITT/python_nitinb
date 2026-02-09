from sqlalchemy import create_engine
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv

load_dotenv()


def connect_db():
    password = quote_plus(os.getenv("password"))
    try:
        engine = create_engine(
            f"mysql+pymysql://root:{password}@localhost:3306/assignment"
        )
        return engine
    except Exception as e:
        print(e, "Error connecting to database")
        return None
