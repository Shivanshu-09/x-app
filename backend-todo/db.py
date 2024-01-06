from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# for postgreSQL database credentials can be written as 
user = 'shivanshu.Sarin'
host = 'localhost'
password = 'password'
port = '5432'
database = 'todo-app'
# for creating connection string
connection_str = f"postgresql://{user}:{password}@{host}:{port}/{database}"
# SQLAlchemy engine
engine = create_engine(connection_str)
# you can test if the connection is made or not

Session = sessionmaker(bind=engine)
session = Session()

try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')