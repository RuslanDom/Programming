import os, sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import asyncio


# from query.core import create_table, insert_data
from query.orm import create_table_orm, insert_data_orm, async_insert_data_orm
create_table_orm()
# insert_data()


asyncio.run(async_insert_data_orm())


