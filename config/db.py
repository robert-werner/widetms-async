import databases
import sqlalchemy

from config.environment import db_user, db_password, db_host, db_port, db

DATABASE_URL = f"postgres://{db_user}:{db_password}@{db_host}:{db_port}/{db}"

database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)