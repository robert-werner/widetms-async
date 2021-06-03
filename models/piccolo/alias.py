from piccolo.table import Table
from piccolo.columns import Varchar, UUID


class Alias(Table, tablename="aliases"):
    id = UUID(primary=True)
    alias = Varchar(length=255)
    description = Varchar(length=1024)
