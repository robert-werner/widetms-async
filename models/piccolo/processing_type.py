from piccolo.table import Table
from piccolo.columns import Varchar, UUID


class ProcessingType(Table, tablename="processing_types"):
    id = UUID(primary=True)
    processing_type = Varchar(length=255)
    description = Varchar(length=1024)
