from pydantic import BaseModel

class Report(BaseModel):
    store_id: int
    uptime_last_hour: int
    uptime_last_day: int
    update_last_week: int
    downtime_last_hour: int
    downtime_last_day: int
    downtime_last_week: int