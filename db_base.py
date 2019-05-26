import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


try:

    # engine = create_engine("mysql+mysqldb://root:anvaya@localhost/punit", max_overflow=0, pool_size=6)

    engine = create_engine(
        "mysql+pymysql://%s:%s@%s/%s?charset=utf8" % ('campaign', 'anvaya123', '3.1.104.251', 'ai_report'),
        max_overflow=0, pool_size=5, pool_recycle=3600,isolation_level="READ UNCOMMITTED")
    Session = sessionmaker(bind=engine)
    session = scoped_session(Session)


except Exception as ex:
    raise Exception("Database connection Expections", ex)
