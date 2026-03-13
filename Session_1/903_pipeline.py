import pandas as pd
from sqlalchemy import (
    create_engine,
    inspect,
    text,
    select,
    MetaData,
    Table,
)

from utils import clean_903_table

# Initialise session variables
filepath = "/workspaces/d2i-intermediate/Session_1/data/903_database.db"



# Read in 903 data from SQL db
engine_903 = create_engine(f"sqlite+pysqlite:///{filepath}")
connection = engine_903.connect()
inspection = inspect(engine_903)

table_names = inspection.get_table_names()

# Uncomment to check database connection
# print(table_names)

metadata_903 = MetaData()

dfs = {}
for table in table_names:
    current_table = Table(table, metadata_903, autoload_with=engine_903)
    with engine_903.connect() as con:
        stmt = select(current_table)
        result = con.execute(stmt).fetchall()
    dfs[table] = pd.DataFrame(result)

# Uncomment to check reading o tables as DFs
#print(dfs.keys())
#print(dfs.values())

for key, df in dfs.items():
    dfs[key] = clean_903_table(df)
    