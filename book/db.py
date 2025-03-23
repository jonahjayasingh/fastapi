from sqlalchemy import create_engine,Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL , connect_args={"check_same_thread": False})

sessionmaker = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()



class BookModel(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    page_count = Column(Integer)
    language = Column(String)

Base.metadata.create_all(bind=engine)


def get_db():
    db: Session = sessionmaker()
    try:
        yield db
    finally:
        db.close()