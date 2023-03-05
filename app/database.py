from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import config, log

settings = config.Settings()
LOG = log.setup_logging(__name__)

POSTGRES_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"

try: 
    engine = create_engine(POSTGRES_DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    LOG.info("Connected successfully to PostgreDB")
except Exception as e:
    LOG.error("%s" %e)