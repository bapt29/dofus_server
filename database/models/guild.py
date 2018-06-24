from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, SmallInteger, BigInteger

from database.core.base import Base


class Guild(Base):
    __tablename__ = "guilds"

    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, name):
        self.name = name
