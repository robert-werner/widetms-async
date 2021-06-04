from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine

from config.environment import DB_NAME, DB_USER, DB_PWD, DB_HOST, DB_PORT

# TODO: connect apps to each other

DB = PostgresEngine(
    config={
        "database": DB_NAME,
        "user": DB_USER,
        "password": DB_PWD,
        "host": DB_HOST,
        "port": DB_PORT,
    }
)

APP_REGISTRY = AppRegistry(
    apps=[
        "home.piccolo_app",
        "forum.piccolo_app",
        "piccolo_admin.piccolo_app",
    ]
)