from sqlalchemy.orm import Session
from models import SwitchInterfaceTraffic, ServerPerformance, Disk

class SwitchInterfaceTrafficDAO:
    def __init__(self, db: Session):
        self.db = db

    def get_traffic_records(self, skip: int = 0, limit: int = 10):
        return self.db.query(SwitchInterfaceTraffic).offset(skip).limit(limit).all()

    def create_traffic_record(self, traffic: SwitchInterfaceTraffic):
        self.db.add(traffic)
        self.db.commit()
        self.db.refresh(traffic)
        return traffic

class ServerPerformanceDAO:
    def __init__(self, db: Session):
        self.db = db

    def get_performance_records(self, skip: int = 0, limit: int = 10):
        return self.db.query(ServerPerformance).offset(skip).limit(limit).all()

    def create_performance_record(self, performance: ServerPerformance):
        self.db.add(performance)
        self.db.commit()
        self.db.refresh(performance)
        return performance