import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


# BEGIN (write your solution here)
def create_db_engine(db_url, echo=False, pool_size=5, max_overflow=10):
    engine = create_engine(db_url, echo=echo, pool_size=pool_size, max_overflow=max_overflow)
    return engine
# END
