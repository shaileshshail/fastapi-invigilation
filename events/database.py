from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./invigilation.db'
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},future=True
)

#future=True ----->https://docs.sqlalchemy.org/en/14/changelog/migration_20.html#migration-core-connection-transaction
SessionLocal =sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db # returns each element 
    finally:
        db.close()
def get_engine():
    return engine
