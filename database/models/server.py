from sqlalchemy import Column, String, Integer, Boolean

from database.core.base import Base


class Server(Base):
    __tablename__ = "servers"

    id = Column(Integer, primary_key=True)
    ip_address = Column(String(15))
    port = Column(Integer)
