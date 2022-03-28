import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:admin123@localhost/hiringdb'

engine = _sql.create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()