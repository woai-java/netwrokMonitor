from dao import SwitchInterfaceTrafficDAO, ServerPerformanceDAO
from models import SwitchInterfaceTraffic, ServerPerformance


class SwitchInterfaceTrafficService:
    def __init__(self, dao: SwitchInterfaceTrafficDAO):
        self.dao = dao

    def get_traffic_records(self, skip: int = 0, limit: int = 10):
        return self.dao.get_traffic_records(skip, limit)

    def create_traffic_record(self, traffic: SwitchInterfaceTraffic):
        return self.dao.create_traffic_record(traffic)

class ServerPerformanceService:
    def __init__(self, dao: ServerPerformanceDAO):
        self.dao = dao

    def get_performance_records(self, skip: int = 0, limit: int = 10):
        return self.dao.get_performance_records(skip, limit)

    def create_performance_record(self, performance: ServerPerformance):
        return self.dao.create_performance_record(performance)