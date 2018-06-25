from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, SmallInteger, BigInteger
from sqlalchemy.orm import relationship

from database.core.base import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)

    account_id = Column(Integer, ForeignKey('accounts.id'), nullable=False)
    server_id = Column(Integer, ForeignKey('servers.id'), nullable=False)

    account = relationship("Account", back_populates="characters", uselist=False)
    server = relationship("Server", back_populates="characters", uselist=False)
    guild = relationship("Guild", back_populates="guilds", uselist=False)

    name = Column(String(255), nullable=False)
    breed = Column(Integer, nullable=False)
    sex = Column(Boolean, nullable=False)
    skin = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False, default=100)
    colors = Column(String(255), nullable=False)
    level = Column(SmallInteger, nullable=False, default=1)
    experience = Column(BigInteger, nullable=False, default=0)
    title = Column(SmallInteger, default=0)
    kamas = Column(BigInteger, nullable=False, default=0)
    map = Column(Integer, nullable=False, default=0)
    cell = Column(SmallInteger, nullable=False, default=0)
    orientation = Column(SmallInteger, nullable=False, default=1)
    saved_waypoints = Column(String(255))
    stat_points = Column(SmallInteger, nullable=False, default=0)
    spell_points = Column(SmallInteger, nullable=False, default=0)
    energy = Column(SmallInteger, nullable=False, default=10000)
    life = Column(SmallInteger, nullable=False, default=100)
    vitality = Column(SmallInteger, nullable=False, default=0)
    wisdom = Column(SmallInteger, nullable=False, default=0)
    strength = Column(SmallInteger, nullable=False, default=0)
    intelligence = Column(SmallInteger, nullable=False, default=0)
    chance = Column(SmallInteger, nullable=False, default=0)
    agility = Column(SmallInteger, nullable=False, default=0)
    alignement = Column(SmallInteger, nullable=False, default=0)
    honor = Column(SmallInteger, nullable=False, default=0)
    dishonor = Column(SmallInteger, nullable=False, default=0)
    pvp_enabled = Column(Boolean, nullable=False, default=False)
    saved_location = Column(String(100))
