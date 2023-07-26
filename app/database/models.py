from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class StoreStatud(Base):
    __tablename__ = "store_status"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer)
    status = Column(String)
    timestamoutc = Column(DateTime)

class MenuHours(Base):
    __tablename__ = "menu_hours"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer)
    day = Column(Integer)
    start_time_local = Column(String)
    end_time_local = Column(String)

class StoreZone(Base):
    __tablename__ = "store_zone"

    id = Column(Integer, primary_key=True, index=True)
    store_id = Column(Integer)
    zone_name = Column(String)