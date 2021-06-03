from piccolo.table import Table
from piccolo.columns import Varchar, UUID


class RemoteSensingDevice(Table, tablename="rs_devices"):
    id = UUID(primary=True)
    rs_device = Varchar(length=255, null=False)
    description = Varchar(length=1024, null=True)
