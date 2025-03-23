from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base  # 修改: 添加 declarative_base 的导入路径

SQLALCHEMY_DATABASE_URL = "postgresql://net_user:pgsql14Che_1@192.168.211.230/net_monitor"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()