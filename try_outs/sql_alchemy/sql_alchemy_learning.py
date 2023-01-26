import psycopg2
from sqlalchemy import create_engine, text, MetaData
from sqlalchemy.orm import registry


engine = create_engine("postgresql+psycopg2:///:memory:", echo=True, future=True)
#meta_data_obj = MetaData()
#print(meta_data_obj)
mapper_registry = registry()
print(mapper_registry.metadata)

#with engine.connect() as conn:
#    result = conn.execute(text("select 'Hello World'"))
#    print(result)
