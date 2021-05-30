import databases
import sqlalchemy

from config.environment import DB_USER, DB_PWD, DB_HOST, DB_NAME, DB_PORT

DB_URL = f"postgresql://{DB_USER}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
database = databases.Database(DB_URL)
metadata = sqlalchemy.MetaData()