from sqlmodel import SQLModel, create_engine
import os

#sqlite_file_name = "database.db"
#sqlite_url = f"sqlite:///{sqlite_file_name}"
mysql_url = f"mysql+pymysql://{os.environ['DB_USER']}:{os.environ['DB_PASSWORD']}@{os.environ['DB_HOST']}:{os.environ['DB_PORT']}/{os.environ['DB_DATABASE']}"


engine = create_engine(mysql_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
