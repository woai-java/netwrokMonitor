from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, SwitchInterfaceTraffic as ModelSwitchInterfaceTraffic, ServerPerformance
from services import SwitchInterfaceTrafficService, ServerPerformanceService
from dao import SwitchInterfaceTrafficDAO, ServerPerformanceDAO
from pydantic import BaseModel
from schemas import SwitchInterfaceTraffic as SchemaSwitchInterfaceTraffic, ServerPerformance

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 实现 get_db 函数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 实现 create_switch_interface_traffic 函数
@app.post("/switch-interface-traffic/", response_model=SchemaSwitchInterfaceTraffic)
def create_switch_interface_traffic(traffic: SchemaSwitchInterfaceTraffic, db: Session = Depends(get_db)):
    dao = SwitchInterfaceTrafficDAO(db)
    service = SwitchInterfaceTrafficService(dao)
    traffic = ModelSwitchInterfaceTraffic(
        switch_id=traffic.switch_id,
        interface_name=traffic.interface_name,
        interface_description=traffic.interface_description,
        traffic_in=traffic.traffic_in,
        traffic_out=traffic.traffic_out,
        timestamp=traffic.timestamp
    )
    return service.create_traffic_record(traffic)

# 实现 read_switch_interface_traffic 函数
@app.get("/switch-interface-traffic/", response_model=list[SchemaSwitchInterfaceTraffic])
def read_switch_interface_traffic(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    dao = SwitchInterfaceTrafficDAO(db)
    service = SwitchInterfaceTrafficService(dao)
    return service.get_traffic_records(skip, limit)

# 实现 create_server_performance 函数
@app.post("/server-performance/", response_model=ServerPerformance)
def create_server_performance(performance: ServerPerformance, db: Session = Depends(get_db)):
    dao = ServerPerformanceDAO(db)
    service = ServerPerformanceService(dao)
    return service.create_performance_record(performance)

# 实现 read_server_performance 函数
@app.get("/server-performance/", response_model=list[ServerPerformance])
def read_server_performance(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    dao = ServerPerformanceDAO(db)
    service = ServerPerformanceService(dao)
    return service.get_performance_records(skip, limit)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)