from pydantic import BaseModel
from datetime import datetime

class SwitchInterfaceTraffic(BaseModel):
    switch_id: str
    interface_name: str
    interface_description: str
    traffic_in: float
    traffic_out: float
    timestamp: datetime

class ServerPerformance(BaseModel):
    server_name: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    timestamp: datetime
    disk_ids: str
    memory_total: float
    cpu_count: int
    cpu_load: str
