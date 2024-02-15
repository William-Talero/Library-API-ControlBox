import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

URLDB = os.environ.get('URL_DATABASE');

engine = create_engine(URLDB);

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine);

Base = declarative_base();

def get_db():
    db = sessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()