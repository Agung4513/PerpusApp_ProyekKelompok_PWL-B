from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Menghubungkan ke database baru kita yang bebas dari bug (perpus_db)
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/perpus_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()