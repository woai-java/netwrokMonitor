from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class SwitchInterfaceTraffic(Base):
    __tablename__ = 'switch_interface_traffic'
    id = Column(Integer, primary_key=True, index=True)
    switch_id = Column(String, index=True)
    interface_name = Column(String, index=True)
    interface_description = Column(String)
    interface_status = Column(String)
    interface_speed = Column(String)
    traffic_in = Column(Float)
    traffic_out = Column(Float)
    timestamp = Column(DateTime, default=func.now())

# 新增磁盘模型
class Disk(Base):
    __tablename__ = 'disks'
    id = Column(Integer, primary_key=True, index=True)
    disk_name = Column(String, index=True)
    disk_size = Column(Float)
    disk_usage = Column(Float)
    timestamp = Column(DateTime, default=func.now())
    server_performance_id = Column(Integer, ForeignKey('server_performance.id'))
    server_performance = relationship("ServerPerformance", back_populates="disks")

class ServerPerformance(Base):
    __tablename__ = 'server_performance'
    id = Column(Integer, primary_key=True, index=True)
    server_name = Column(String, index=True)
    cpu_usage = Column(Float)
    memory_usage = Column(Float)
    disk_usage = Column(Float)
    timestamp = Column(DateTime, default=func.now())
    disk_ids = Column(String)
    memory_total = Column(Float)
    cpu_count = Column(Integer)
    cpu_load = Column(String)
    disks = relationship("Disk", back_populates="server_performance")