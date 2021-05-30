import ormar

from config.db import metadata
from config.db import database


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
